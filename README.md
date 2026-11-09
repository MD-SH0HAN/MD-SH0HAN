<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="Dark%20Header.svg" />
    <source media="(prefers-color-scheme: light)" srcset="Light%20Header.svg" />
    <img src="Light%20Header.svg" width="100%" alt="MD Shohan — DevOps Engineering" />
  </picture>
</p>

<h3 align="center">ASPIRING DEVOPS ENGINEER</h3>
<p align="center"><strong>CI/CD AUTOMATION · CLOUD INFRASTRUCTURE · CONTAINERS · OBSERVABILITY</strong></p>

<p align="center">
  <a href="https://md-sh0han.github.io/PORTFOLIO/"><img src="https://img.shields.io/badge/Portfolio-Explore-0A101F?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Explore portfolio" /></a>
  &nbsp;
  <a href="https://github.com/MD-SH0HAN/PORTFOLIO"><img src="https://img.shields.io/badge/DevOps_Projects-View-181717?style=for-the-badge&logo=github&logoColor=white" alt="View DevOps projects" /></a>
  &nbsp;
  <a href="mailto:mohammad.and.shohan@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Contact by email" /></a>
</p>

<p align="center">
  <a href="#about-me">About</a> &nbsp;·&nbsp;
  <a href="#devops-focus">DevOps Focus</a> &nbsp;·&nbsp;
  <a href="#featured-projects">Projects</a> &nbsp;·&nbsp;
  <a href="#technology-toolkit">Toolkit</a> &nbsp;·&nbsp;
  <a href="#engineering-practices">Practices</a> &nbsp;·&nbsp;
  <a href="#learning-roadmap">Learning</a> &nbsp;·&nbsp;
  <a href="#connect">Connect</a>
</p>

---

## About Me

I'm **MD Shohan**, a **Computer Science & Engineering undergraduate at Bangladesh University**, based in Bangladesh, and building my career toward **DevOps Engineering**.

I'm interested in the engineering practices that make software delivery reliable and repeatable: **CI/CD automation, Linux and networking, cloud infrastructure, Infrastructure as Code, containers, Kubernetes, monitoring, and deployment security**.

I learn by building and documenting practical projects. My repositories show the implementation, configuration, validation approach, and current limitations of each project. I clearly distinguish locally runnable work and source-ready infrastructure from services that have actually been deployed.

- 🎯 **Career goal:** Build the skills and practical experience required for an entry-level DevOps Engineer role.
- 🎓 **Education:** BSc in Computer Science & Engineering — Bangladesh University.
- 🌏 **Based in:** Bangladesh.
- ⚙️ **Primary interests:** CI/CD, automation, cloud infrastructure, containers, Kubernetes, and observability.
- 🧪 **Portfolio focus:** A local observability lab and source-controlled delivery, infrastructure, and Kubernetes configurations.

> **My approach:** Understand the system, automate repeatable tasks, validate changes, apply secure defaults, observe runtime behavior, and document the result.

## DevOps Focus

I am developing practical capability across the software delivery lifecycle:

| DevOps area | Tools and concepts in my work or learning path |
|---|---|
| **Source control and scripting** | Git, Python, Linux, Bash |
| **CI/CD and release automation** | GitHub Actions, automated tests, container builds, release workflows |
| **Containers and registries** | Docker, Docker Compose, GitHub Container Registry (GHCR) |
| **Cloud and Infrastructure as Code** | AWS, Terraform, VPC, IAM, ECR |
| **Orchestration and packaging** | Kubernetes, Kustomize, Helm |
| **GitOps and deployment management** | Argo CD, declarative configuration, immutable image references |
| **Security and supply-chain checks** | Trivy, image scanning, CycloneDX SBOM, RBAC, least privilege |
| **Monitoring and observability** | Prometheus, Grafana, metrics, alert rules, health checks |
| **Reliability foundations** | Testing, resource controls, probes, disruption budgets, recovery thinking |

The table describes technologies represented in my projects or learning path; it does not imply production experience with every tool.

## Featured Projects

These projects are selected to show how I am learning the DevOps workflow—from building and validating an application to packaging, infrastructure configuration, deployment patterns, and observability.

### 1. Observability Reference Lab

[**View project source**](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory)

A locally runnable reference service and monitoring setup containing:

- Python HTTP API and automated tests.
- Dockerfile and Docker Compose configuration.
- Prometheus metrics and alert rules.
- Provisioned Grafana dashboard.

**Status:** Local reference implementation. Docker Compose run instructions are included; this is not presented as a production service.

### 2. Container Image CI Workflow

[**View GitHub Actions workflow**](https://github.com/MD-SH0HAN/PORTFOLIO/blob/main/.github/workflows/laboratory-image.yml)

A source-controlled pipeline designed to demonstrate:

- API test execution.
- Container image build.
- Trivy vulnerability scanning gate.
- CycloneDX SBOM generation.
- GHCR publication step and image digest output.

**Status:** Workflow source is included. Successful remote registry publication has not been verified, so I do not claim a completed release.

### 3. Kubernetes Workload Baseline

[**View Kubernetes configurations**](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/kubernetes)

Kubernetes deployment configuration with operational and security considerations:

- Kustomize base and environment overlays.
- Startup/readiness/liveness probe configuration where applicable.
- CPU and memory requests and limits.
- Non-root security context and read-only root filesystem.
- RBAC, Horizontal Pod Autoscaler, PodDisruptionBudget, and NetworkPolicy.

**Status:** Source-ready configuration. No live cluster deployment is claimed.

### 4. AWS Infrastructure with Terraform

[**View Terraform source**](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/infrastructure/terraform)

An infrastructure foundation covering:

- Multi-Availability Zone VPC layout.
- Public and private subnet configuration.
- Amazon ECR repository with scan-on-push and lifecycle policy.
- Explicitly opt-in NAT and EKS resources.

**Status:** Source-ready Terraform. It has not been applied to an AWS account.

### Additional DevOps and Delivery Work

| Project | What it contains | Status |
|---|---|---|
| [Helm Chart](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/helm/laboratory-api) | Parameterized workload chart, probes, security settings, autoscaling, disruption budget, NetworkPolicy, and values schema | Source-ready; chart lint/render is configured in CI; no cluster release claimed |
| [Argo CD GitOps Application](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/gitops) | Argo CD Application for the Helm chart, automated sync, prune, self-heal, and content-digest image pinning support | Source-ready; no live Argo CD sync claimed |
| [Portfolio Website](https://md-sh0han.github.io/PORTFOLIO/) · [Source](https://github.com/MD-SH0HAN/PORTFOLIO) | Project documentation, case studies, architecture explanations, and portfolio presentation | Built static website |

<sub>**Project status is intentional:** locally runnable means it can be run in a local environment; source-ready means configuration is present but not necessarily deployed; workflow source does not prove a successful remote release.</sub>

## Technology Toolkit

I organize my toolkit by how each technology currently appears in my work. **These categories are more meaningful than treating every badge as the same level of proficiency.**

### Used in current portfolio implementations

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
</p>

### Infrastructure and delivery configurations in my repositories

<p>
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="Amazon Web Services" />
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="Terraform" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/Kustomize-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kustomize" />
  <img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" alt="Helm" />
  <img src="https://img.shields.io/badge/Argo_CD-EF7B4D?style=flat-square&logo=argo&logoColor=white" alt="Argo CD" />
  <img src="https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=aqua&logoColor=white" alt="Trivy" />
  <img src="https://img.shields.io/badge/GHCR-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub Container Registry" />
</p>

### Foundations I'm actively developing

<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />
  <img src="https://img.shields.io/badge/Networking-TCP%2FIP-00599C?style=flat-square" alt="Networking and TCP/IP" />
  <img src="https://img.shields.io/badge/IAM_&_Cloud_Security-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="IAM and cloud security" />
  <img src="https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white" alt="OpenTelemetry" />
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible" />
  <img src="https://img.shields.io/badge/SRE_&_Reliability-44546A?style=flat-square" alt="SRE and reliability" />
</p>

## Engineering Practices

The practices I want my DevOps work to demonstrate are:

- **Automate repeatable work:** use scripts and pipelines to reduce manual, error-prone steps.
- **Keep infrastructure reviewable:** define infrastructure and deployment configuration as code and track changes in Git.
- **Build and release responsibly:** test changes, scan images, generate software bills of materials, and prefer immutable artifact references.
- **Apply secure defaults:** use least privilege, non-root containers, explicit network boundaries, and avoid exposing secrets.
- **Make systems observable:** use metrics, health checks, dashboards, and actionable alert rules.
- **Plan for failure:** consider resource limits, readiness, disruption, recovery, and safe cleanup.
- **Document honestly:** state what was tested, what is configured, what is running, and what remains to be done.

## Learning Roadmap

My current development priorities follow the DevOps lifecycle:

1. **Linux and systems:** command line, processes, permissions, services, filesystems, Bash, and troubleshooting.
2. **Networking:** TCP/IP, DNS, HTTP/HTTPS, TLS, routing, ports, and network troubleshooting.
3. **Automation and CI/CD:** Python, Bash, Git workflows, pipeline design, test automation, and release practices.
4. **Cloud and IaC:** AWS fundamentals, IAM, VPC networking, Terraform state/modules, and cost-aware infrastructure.
5. **Containers and Kubernetes:** image fundamentals, container security, workloads, services, probes, resources, Helm, and Kustomize.
6. **GitOps and delivery security:** Argo CD, image scanning, SBOMs, artifact traceability, and deployment controls.
7. **Observability and reliability:** metrics, logs, traces, alert quality, SLIs/SLOs, incident response, and recovery exercises.

I aim to build depth in the fundamentals and demonstrate progress through working, documented projects—not simply add more tools to a badge collection.

## GitHub Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MD-SH0HAN/MD-SH0HAN/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MD-SH0HAN/MD-SH0HAN/output/github-contribution-grid-snake.svg" />
    <img src="https://raw.githubusercontent.com/MD-SH0HAN/MD-SH0HAN/output/github-contribution-grid-snake.svg" alt="GitHub contribution activity" width="100%" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./profile/stats-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./profile/stats-light.svg" />
    <img src="./profile/stats-light.svg" alt="GitHub contribution statistics" height="180" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./profile/top-langs-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./profile/top-langs-light.svg" />
    <img src="./profile/top-langs-light.svg" alt="Most-used programming languages" height="180" />
  </picture>
</p>
<p align="center"><em>Learn deliberately. Build reproducibly. Operate responsibly. Make developers more effective.</em></p>


## Connect With Me

<p align="center">
  <a href="mailto:mohammad.and.shohan@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  &nbsp;
  <a href="https://github.com/MD-SH0HAN">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  &nbsp;
  <a href="https://outlook.office.com/mail/deeplink/compose?to=mohammad.and.shohan%40outlook.com">
    <img src="https://img.shields.io/badge/Outlook-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white" alt="Outlook" />
  </a>
</p>

## Social

<p align="center">
  <a href="https://discord.com/users/1221600292915773468">
    <img src="https://cdn.simpleicons.org/discord/5865F2" width="35" height="35" alt="Discord" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.reddit.com/user/MD-SH0HAN/">
    <img src="https://cdn.simpleicons.org/reddit/FF4500" width="35" height="35" alt="Reddit" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.instagram.com/_md.shohan_/">
    <img src="https://cdn.simpleicons.org/instagram/E4405F" width="35" height="35" alt="Instagram" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.facebook.com/mohammad.and.shohan">
    <img src="https://cdn.simpleicons.org/facebook/0866FF" width="35" height="35" alt="Facebook" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.threads.com/@_md.shohan_">
    <img src="https://cdn.simpleicons.org/threads/8B8B8B" width="35" height="35" alt="Threads" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.twitch.tv/md_shohan">
    <img src="https://cdn.simpleicons.org/twitch/9146FF" width="35" height="35" alt="Twitch" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.tumblr.com/md-shohan">
    <img src="https://cdn.simpleicons.org/tumblr/36465D" width="35" height="35" alt="Tumblr" />
  </a>
</p>
