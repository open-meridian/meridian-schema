SHELL := /bin/bash
PY    := python3

# The generated output is vendored under gen/ and reviewed like any other code.
# Regeneration happens in a pinned container, so the host needs only Docker.
GEN_DIR   := gen
SCRATCH   := .codegen-scratch
RUST_VERSION  := 1.90
DOCKER    := DOCKER_BUILDKIT=1 docker

.PHONY: help ci-local ci-local-deep install-hooks ci-mirror-check codegen check-codegen \
        check-pb-compiles check-pb-imports clean

help:
	@echo "  make ci-local       run every gate (the pre-push gate, and what CI mirrors)"
	@echo "  make codegen        regenerate Rust and Python bindings into $(GEN_DIR)/"
	@echo "  make check-codegen  fail if $(GEN_DIR)/ is stale against proto/"
	@echo "  make install-hooks  point git at hooks/ so push fires ci-local"
	@echo "  make check-pb-compiles / check-pb-imports   generated output actually works"

# Local green is the completion signal; CI is confirmation.
ci-local: ci-mirror-check check-codegen check-pb-compiles check-pb-imports
	@echo
	@echo "ci-local: GREEN"

ci-local-deep: ci-local

ci-mirror-check:
	@$(PY) tools/ci_mirror_check.py --repo-root .

# Regenerate in place. The only sanctioned way to change anything under gen/.
codegen:
	@rm -rf $(GEN_DIR)
	@$(DOCKER) build -f Dockerfile.codegen --target export \
		--output type=local,dest=$(GEN_DIR) .
	@echo "codegen: wrote $(GEN_DIR)/rust and $(GEN_DIR)/python"

# Generate into a scratch directory and compare. Vendored output that does not
# match a fresh generation is either a stale checkout or a hand-edit, and both
# are the same bug: something downstream is building against types the schema
# does not describe.
check-codegen:
	@rm -rf $(SCRATCH)
	@$(DOCKER) build -f Dockerfile.codegen --target export \
		--output type=local,dest=$(SCRATCH) . >/dev/null 2>&1 \
		|| { echo "check-codegen: generation failed; run 'make codegen' to see why" >&2; exit 1; }
	@if diff -r -q $(GEN_DIR) $(SCRATCH) >/dev/null 2>&1; then \
		rm -rf $(SCRATCH); \
		echo "check-codegen OK: $(GEN_DIR)/ matches a fresh generation"; \
	else \
		echo "check-codegen FAILED: $(GEN_DIR)/ is stale or hand-edited" >&2; \
		diff -r $(GEN_DIR) $(SCRATCH) | head -40 >&2; \
		rm -rf $(SCRATCH); \
		echo >&2; \
		echo "Run 'make codegen' and commit the result. Never edit $(GEN_DIR)/ by hand." >&2; \
		exit 1; \
	fi

# Generated output that does not build is worse than none: it fails downstream,
# far from the schema change that caused it. Both checks are cheap and run here.
check-pb-compiles:
	@$(DOCKER) build -f Dockerfile.codegen --target pb-check . >/dev/null 2>&1 \
		|| { echo "check-pb-compiles FAILED: generated Rust does not compile;" >&2; \
		     echo "  see it with: DOCKER_BUILDKIT=1 docker build -f Dockerfile.codegen --target pb-check ." >&2; \
		     exit 1; }
	@echo "check-pb-compiles OK: generated Rust crate builds"

check-pb-imports:
	@$(PY) tools/check_pb_imports.py --gen $(GEN_DIR)/python

install-hooks:
	@git config core.hooksPath hooks
	@echo "hooks installed: git push now runs 'make ci-local' first"

clean:
	@rm -rf $(SCRATCH)
