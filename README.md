<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="Dark%20Header.svg" />
    <source media="(prefers-color-scheme: light)" srcset="Light%20Header.svg" />
    <img src="Light%20Header.svg" width="100%" alt="MD Shohan — Cloud, DevOps and Platform Engineering" />
  </picture>
</p>

<h3 align="center">CLOUD ENGINEERING · DEVOPS · PLATFORM ENGINEERING</h3>

<p align="center">
  <a href="#about">About</a> ·
  <a href="#featured-engineering-work">Projects</a> ·
  <a href="#technology-toolkit">Toolkit</a> ·
  <a href="#engineering-principles">Principles</a> ·
  <a href="#current-learning-focus">Learning</a> ·
  <a href="#connect">Connect</a>
</p>

<p align="center">
  <a href="https://md-sh0han.github.io/PORTFOLIO/"><img src="https://img.shields.io/badge/Portfolio-Explore-0A101F?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Explore portfolio" /></a>
  <a href="https://github.com/MD-SH0HAN/PORTFOLIO"><img src="https://img.shields.io/badge/Engineering_Repository-View-181717?style=for-the-badge&logo=github&logoColor=white" alt="View engineering repository" /></a>
  <a href="mailto:mohammad.and.shohan@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Contact by email" /></a>
</p>

---

## About

I'm **MD Shohan**, a **Computer Science & Engineering undergraduate at Bangladesh University**, based in Bangladesh. I'm building my engineering career across **Cloud Engineering, DevOps, and Platform Engineering**, with a focus on infrastructure automation, cloud-native systems, CI/CD, observability, reliability, and developer experience.

I like turning repeatable engineering work into workflows that are **automated, reproducible, secure by default, observable, and documented**. I use my public repositories to develop practical skills and show the implementation details, configuration, validation approach, and limitations behind my work.

- 🎓 **Education:** BSc in Computer Science & Engineering — Bangladesh University
- ☁️ **Career direction:** Cloud infrastructure, DevOps automation, and platform engineering
- 🧪 **Current work:** A local observability lab and source-ready Kubernetes, Terraform, GitOps, and Backstage assets
- 🎯 **Long-term focus:** Reliable infrastructure and useful self-service workflows for software teams

> **My engineering approach:** Understand the system, automate repeatable work, apply secure defaults, validate failure paths, document operational decisions, and improve through feedback.

## Featured Engineering Work

My portfolio is organized around practical engineering evidence—not a checklist of tools. The projects below cover application observability, container delivery, infrastructure, and cloud-native deployment patterns.

| Project | What it demonstrates | Status |
|---|---|---|
| [Observability Reference Lab](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory) | Python HTTP API, Dockerfile, Docker Compose, Prometheus metrics and alert rules, provisioned Grafana dashboard, and automated tests | **Local reference implementation** — Docker Compose run instructions included; not presented as a production service |
| [Kubernetes Workload Baseline](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/kubernetes) | Kustomize base and overlays, probes, resource requests and limits, non-root security context, read-only root filesystem, RBAC, HPA, PDB, and NetworkPolicy | **Source-ready** — no live cluster deployment claimed |
| [Container Image Release Workflow](https://github.com/MD-SH0HAN/PORTFOLIO/blob/main/.github/workflows/laboratory-image.yml) | GitHub Actions workflow for API tests, image build, Trivy vulnerability gate, CycloneDX SBOM, GHCR publication, and digest output | **Workflow source included** — remote registry publication has not been verified |
| [AWS / Terraform Foundation](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/infrastructure/terraform) | Two-availability-zone VPC foundation, public and private subnets, ECR with scan-on-push and lifecycle policy, and explicitly opt-in NAT/EKS resources | **Source-ready** — not applied to an AWS account |

### Additional Platform Engineering Work

| Project | Repository contents | Status |
|---|---|---|
| [Helm Chart](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/helm/laboratory-api) | Parameterized workload chart, health probes, security defaults, autoscaling, disruption budget, NetworkPolicy, and values schema | **Source-ready** — chart lint/render is configured in CI; no cluster release claimed |
| [Argo CD GitOps Application](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/gitops) | Argo CD Application tracking the Helm chart with automated sync, prune, self-heal, and content-digest image pinning support | **Source-ready** — no live Argo CD sync claimed |
| [Backstage Platform Starter](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/platform/backstage) | Catalog Group, Component, and API entities; a Python-service Scaffolder template; and a service skeleton with tests and CI workflow | **Starter source included** — no running Backstage installation or live template execution claimed |
| [Portfolio Website](https://md-sh0han.github.io/PORTFOLIO/) · [Source](https://github.com/MD-SH0HAN/PORTFOLIO) | Responsive static site, accessible navigation, project case studies, architecture explanations, and clearly labelled synthetic demonstrations | **Built static website** |

<sub>**Status key:** “Local reference implementation” means the project is designed to run locally; “Source-ready” means configuration and source are provided, not that they have been deployed; “Workflow source included” does not imply a successful remote release.</sub>

## Technology Toolkit

The categories below describe how technologies appear in my portfolio and learning path. **A badge indicates repository use or study—not equal proficiency or professional production experience.**

### Implemented in the current portfolio

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
</p>

### Infrastructure and platform configurations in the portfolio

<p>
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="Amazon Web Services" />
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="Terraform" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/Kustomize-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kustomize" />
  <img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" alt="Helm" />
  <img src="https://img.shields.io/badge/Argo_CD-EF7B4D?style=flat-square&logo=argo&logoColor=white" alt="Argo CD" />
  <img src="https://img.shields.io/badge/GHCR-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub Container Registry" />
  <img src="https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=aqua&logoColor=white" alt="Trivy" />
  <img src="https://img.shields.io/badge/Backstage-9BF0E1?style=flat-square&logo=backstage&logoColor=black" alt="Backstage" />
</p>

### Foundations I'm continuing to develop

<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />
  <img src="https://img.shields.io/badge/Networking-TCP%2FIP-00599C?style=flat-square" alt="Networking and TCP/IP" />
  <img src="https://img.shields.io/badge/IAM_&_Cloud_Security-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="IAM and cloud security" />
  <img src="https://img.shields.io/badge/SRE_&_Reliability-44546A?style=flat-square" alt="SRE and reliability" />
  <img src="https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white" alt="OpenTelemetry" />
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible" />
</p>

## Engineering Principles

| Principle | How I apply it |
|---|---|
| **Infrastructure as Code** | Keep infrastructure reviewable, repeatable, and separated by environment. |
| **Secure by default** | Prefer least privilege, non-root workloads, restricted capabilities, explicit network boundaries, and secret-safe workflows. |
| **Automation with feedback** | Validate changes in CI and make failures, logs, and next steps understandable. |
| **GitOps and traceability** | Version-control desired deployment state and use immutable image references for reviewed releases. |
| **Observability and reliability** | Use metrics, health checks, alerts, and tests to understand service behavior and failure recovery. |
| **Platform as a product** | Build templates and self-service workflows around developer needs, usability, and ownership. |
| **Cost awareness** | Consider cloud cost, resource limits, and safe cleanup as part of infrastructure design. |
| **Honest engineering evidence** | Distinguish tested behavior, source-ready configuration, simulations, and actual deployments. |

## Current Learning Focus

I'm developing breadth across the systems that support dependable cloud and DevOps work, then building deeper practical capability in each area.

1. **Systems foundations:** Linux, operating systems, networking, DNS, TLS, Git, Python, and Bash.
2. **Cloud and infrastructure:** AWS networking and IAM, Terraform modules and state, security boundaries, and cost-aware resource design.
3. **Containers and orchestration:** Docker, Kubernetes workloads, probes, resource management, RBAC, NetworkPolicy, and Helm.
4. **Delivery and GitOps:** CI validation, image scanning, SBOMs, immutable image references, GitHub Actions, and Argo CD.
5. **Observability and SRE:** Metrics, logs, traces, alert testing, SLIs/SLOs, incident response, and recovery exercises.
6. **Developer platforms and operations:** Backstage, software templates, golden paths, policy as code, FinOps, and disaster recovery.

I prefer learning a focused set of complementary tools deeply rather than collecting badges across every product in the ecosystem.

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

## Connect

<p align="center">
  <a href="https://md-sh0han.github.io/PORTFOLIO/"><img src="https://img.shields.io/badge/Portfolio-Visit-0A101F?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Visit portfolio" /></a>
  <a href="https://github.com/MD-SH0HAN"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="Follow on GitHub" /></a>
  <a href="mailto:mohammad.and.shohan@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email me" /></a>
</p>

<p align="center">
  <a href="https://gitlab.com/MD-SHOHAN">GitLab</a> ·
  <a href="https://hub.docker.com/u/mdsh0han">Docker Hub</a> ·
  <a href="https://vercel.com/md-shohan">Vercel</a> ·
  <a href="https://www.facebook.com/mohammad.and.shohan">Facebook</a> ·
  <a href="https://www.instagram.com/_md.shohan_">Instagram</a> ·
  <a href="https://www.threads.com/@_md.shohan_">Threads</a> ·
  <a href="https://www.twitch.tv/md_shohan">Twitch</a> ·
  <a href="https://www.tumblr.com/md-shohan">Tumblr</a> ·
  <a href="https://www.reddit.com/user/MD-SH0HAN/">Reddit</a> ·
  <a href="https://discord.com/users/1221600292915773468">Discord</a>
</p>

<p align="center"><em>Learn deliberately. Build reproducibly. Operate responsibly. Make developers more effective.</em></p>
