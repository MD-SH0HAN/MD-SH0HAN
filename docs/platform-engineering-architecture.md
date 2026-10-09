# From Beginner to Platform Engineering

A practical learning path and a target architecture for a small, evolving Internal Developer Platform (IDP). This is a **reference design**, not a claim that every component is already implemented. Keep only the components that your project actually uses as you build it.

## 1. Reference architecture: an Internal Developer Platform

```mermaid
flowchart TB
    DEV["Application developers"]

    subgraph DX["1 · Developer experience"]
        direction TB
        INTERFACE["Portal (optional) · CLI · API"]
        CATALOG["Service catalog · documentation · ownership"]
        GOLDEN["Golden paths · starter templates · standard defaults"]
        INTERFACE --> CATALOG
        INTERFACE --> GOLDEN
    end

    DEV --> INTERFACE

    subgraph SELF["2 · Self-service orchestration"]
        direction TB
        SCAFFOLD["Create a repository and service baseline"]
        PROVISION["Provision infrastructure with Terraform / Ansible"]
        GUARDRAILS["Apply identity, policy and configuration guardrails"]
    end

    GOLDEN --> SCAFFOLD
    GOLDEN --> PROVISION
    GOLDEN --> GUARDRAILS

    subgraph DELIVERY["3 · Software delivery and supply chain"]
        direction TB
        REPO["GitHub repository · pull requests · code review"]
        CI["CI: lint · tests · dependency and security checks"]
        IMAGE["Build and version a container image"]
        REGISTRY["Container registry: GHCR or equivalent"]
        CONFIG["Deployment configuration: Helm / Kustomize"]
        REPO --> CI
        CI --> IMAGE
        IMAGE --> REGISTRY
        CI -. "updates approved image tag" .-> CONFIG
    end

    SCAFFOLD --> REPO

    subgraph RUNTIME["4 · Cloud and runtime foundation"]
        direction TB
        CLOUD["Cloud foundation: IAM · network · DNS · compute · storage"]
        CLUSTER["Kubernetes or another suitable runtime"]
        ROUTING["Ingress / load balancer · service routing"]
        APP["Application workloads"]
        DATA["Database or object storage, when needed"]
        CLOUD --> CLUSTER
        CLUSTER --> ROUTING
        ROUTING --> APP
        APP --> DATA
    end

    PROVISION --> CLOUD
    GITOPS["GitOps reconciler: Argo CD / Flux, if adopted"]
    CONFIG --> GITOPS
    GITOPS --> CLUSTER
    REGISTRY -. "runtime pulls the approved image" .-> APP

    subgraph CONTROL["5 · Cross-cutting security and governance"]
        direction TB
        IDENTITY["Identity · least privilege · access control"]
        SECRETS["Secret and key management"]
        POLICY["Policy checks · image provenance · configuration validation"]
    end

    GUARDRAILS --> POLICY
    CI -. "checks block unsafe builds" .-> POLICY
    PROVISION -. "validate infrastructure changes" .-> POLICY
    IDENTITY -. "authenticate and authorize" .-> INTERFACE
    IDENTITY -.-> CLOUD
    IDENTITY -.-> CLUSTER
    SECRETS -. "provide runtime secrets securely" .-> APP

    subgraph OPERATIONS["6 · Operations and feedback"]
        direction TB
        OBS["Observability: metrics · logs · traces · dashboards"]
        RELIABILITY["Reliability: SLOs · alerts · runbooks · recovery"]
        COST["Cost · capacity · resource utilization"]
        FEEDBACK["Developer feedback · adoption · friction points"]
        OBS --> RELIABILITY
        OBS --> FEEDBACK
        COST --> FEEDBACK
    end

    APP --> OBS
    CLUSTER --> OBS
    CLOUD --> COST
    RELIABILITY -. "improve paved roads" .-> GOLDEN
    FEEDBACK -. "prioritize platform improvements" .-> CATALOG
    COST -. "optimize provisioning defaults" .-> PROVISION

    classDef people fill:#eaf2ff,stroke:#3569a8,color:#142d4e,stroke-width:1.5px
    classDef experience fill:#eaf2ff,stroke:#3569a8,color:#142d4e
    classDef automation fill:#efe8ff,stroke:#7552a8,color:#2d2045
    classDef delivery fill:#e4f5eb,stroke:#32835a,color:#153d2b
    classDef runtime fill:#fff2d9,stroke:#b87b1b,color:#5b3b0c
    classDef security fill:#ffe7e7,stroke:#bd4b4b,color:#5a2020
    classDef ops fill:#e5f4f7,stroke:#347e8a,color:#163c43

    class DEV people
    class INTERFACE,CATALOG,GOLDEN experience
    class SCAFFOLD,PROVISION,GUARDRAILS automation
    class REPO,CI,IMAGE,REGISTRY,CONFIG,GITOPS delivery
    class CLOUD,CLUSTER,ROUTING,APP,DATA runtime
    class IDENTITY,SECRETS,POLICY security
    class OBS,RELIABILITY,COST,FEEDBACK ops
```

### How to read it

- **Developers consume the platform** through a portal, CLI, API, or documented workflow. A portal is optional; self-service can start with templates and automation.
- **Golden paths standardize common work**—for example, starting a service, creating a repository, running checks, and deploying safely.
- **CI builds and validates artifacts**, while the deployment process promotes a known image version into the runtime environment.
- **Infrastructure automation provisions the foundation**. A GitOps controller is optional and should only be shown as implemented when the project uses one.
- **Security and operations are cross-cutting capabilities**, not final steps. Feedback, reliability, cost and developer experience should influence how the platform evolves.

## 2. The learning path: fundamentals to platform engineering

```mermaid
flowchart TB
    A["1 · Foundations<br/>Linux · terminal · Git<br/>Networking · DNS · HTTP · TLS · SSH"]
    B["2 · Scripting and software basics<br/>Bash · Python · APIs · YAML / JSON<br/>Testing · debugging"]
    C["3 · Source control and CI<br/>GitHub workflows · lint · tests<br/>Build automation"]
    D["4 · Containers and artifacts<br/>Docker · Compose · registries<br/>Versioning · image hygiene"]
    E["5 · Cloud and infrastructure as code<br/>AWS or another cloud · IAM · networking<br/>Terraform · Ansible · state"]
    F["6 · Orchestration and delivery<br/>Kubernetes · Helm · deployment strategies<br/>GitOps concepts"]
    G["7 · Security and reliability<br/>Secrets · least privilege · scanning<br/>Metrics · logs · traces · SLOs · recovery"]
    H["8 · Platform engineering<br/>Developer needs · golden paths<br/>Templates · self-service APIs / workflows"]
    I["Capstone<br/>One documented, secure, repeatable path<br/>from new service to observable deployment"]

    A --> B --> C --> D --> E --> F --> G --> H --> I

    classDef foundation fill:#eaf2ff,stroke:#3569a8,color:#142d4e
    classDef delivery fill:#e4f5eb,stroke:#32835a,color:#153d2b
    classDef platform fill:#efe8ff,stroke:#7552a8,color:#2d2045
    class A,B foundation
    class C,D,E,F,G delivery
    class H,I platform
```

This is a guide, not a rigid ladder. Build small projects at each stage and revisit earlier skills whenever a project requires them.

## 3. Suggested first capstone

Start small. Create a minimal application and make one supported path that can:

1. Create a repository from a documented template.
2. Run formatting, linting, tests, and appropriate security checks in CI.
3. Build and publish a versioned container image.
4. Provision only the infrastructure needed for the demo.
5. Deploy the selected image using a documented, repeatable process.
6. Expose health checks and basic logs/metrics, with a short runbook.
7. Document rollback, teardown, costs and known limitations.

Only add a portal, a GitOps controller, policy engine, or Kubernetes if it solves a real problem for the capstone. For a learning project, a reliable small golden path is better than a large diagram full of tools you have not used.

## References

- [GitHub Docs: Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
- [CNCF: What is Platform Engineering?](https://www.cncf.io/blog/2025/11/19/what-is-platform-engineering/)
- [CNCF: Internal developer platform vs. internal developer portal vs. PaaS](https://www.cncf.io/blog/2023/12/08/internal-developer-platform-vs-internal-developer-portal-vs-paas/)
