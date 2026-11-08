<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="Dark%20Header.svg" />
    <source media="(prefers-color-scheme: light)" srcset="Light%20Header.svg" />
    <img src="Light%20Header.svg" width="100%" alt="MD Shohan" />
  </picture>
</p>

<p align="center">
  <strong>CLOUD ENGINEERING · DEVOPS ENGINEERING · PLATFORM ENGINEERING</strong>
</p>

<p align="center">
  <a href="#about-me">About</a> &nbsp;·&nbsp;
  <a href="#engineering-work">Engineering Work</a> &nbsp;·&nbsp;
  <a href="#technology-toolkit">Technology Toolkit</a> &nbsp;·&nbsp;
  <a href="#engineering-principles">Engineering Principles</a> &nbsp;·&nbsp;
  <a href="#current-learning-direction">Learning Direction</a> &nbsp;·&nbsp;
  <a href="#connect">Connect</a>
</p>

---

## About Me

I'm **MD Shohan**, a **Computer Science & Engineering undergraduate at Bangladesh University**. I'm building my career in **Cloud Engineering → DevOps Engineering → Platform Engineering**, with a strong interest in infrastructure automation, cloud-native systems, observability, reliability, and developer experience.

I enjoy turning repeatable engineering work into infrastructure and delivery workflows that are **reproducible, secure by default, observable, documented, and easier for developers to use**. My public portfolio records the code, configurations, tests, and limitations of the projects I'm building as I develop practical engineering skills.

- 🎓 **Education:** BSc in Computer Science & Engineering — Bangladesh University
- 🌏 **Based in:** Bangladesh
- ☁️ **Career direction:** Cloud infrastructure, DevOps automation, and platform engineering
- 🧪 **Current work:** A local observability lab and source-ready Kubernetes, Terraform, GitOps, and Backstage platform assets
- 🎯 **Long-term focus:** Reliable infrastructure and useful self-service workflows for software teams

> **Engineering approach:** Understand the system, automate repeatable work, apply secure defaults, test failure paths, document operational decisions, and measure the outcome.

<p align="center">
  <a href="https://md-sh0han.github.io/PORTFOLIO/"><img src="https://img.shields.io/badge/Portfolio-Explore-0A101F?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Explore my portfolio" /></a>
  &nbsp;
  <a href="https://github.com/MD-SH0HAN/PORTFOLIO"><img src="https://img.shields.io/badge/Engineering_Repository-View-181717?style=for-the-badge&logo=github&logoColor=white" alt="View engineering repository" /></a>
  &nbsp;
  <a href="mailto:mohammad.and.shohan@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Contact by email" /></a>
</p>

## Engineering Work

My portfolio is organized around practical evidence rather than a list of tools. The status labels below are intentional: **source code is not the same as a deployed service**, and a local lab is not production infrastructure.

| Project | What the repository contains | Status |
|---|---|---|
| [Observability Reference Lab](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory) | Python HTTP API, Dockerfile, Docker Compose, Prometheus metrics and alert rules, provisioned Grafana dashboard, and automated tests | **Local reference implementation** — Docker Compose run instructions included; not presented as a production service |
| [Kubernetes Workload Baseline](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/kubernetes) | Kustomize base and environment overlays, probes, resource requests/limits, non-root security context, read-only root filesystem, RBAC, HPA, PDB, and NetworkPolicy | **Source-ready** — no live cluster deployment claimed |
| [Helm Chart](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/helm/laboratory-api) | Parameterized workload chart, health probes, security defaults, autoscaling, disruption budget, network policy, and values schema | **Source-ready** — chart lint/render is configured in CI; no cluster release claimed |
| [AWS / Terraform Foundation](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/infrastructure/terraform) | Two-availability-zone VPC foundation, public/private subnets, ECR repository with scan-on-push and lifecycle policy, and explicitly opt-in NAT/EKS resources | **Source-ready** — not applied to an AWS account |
| [Container Image Release Workflow](https://github.com/MD-SH0HAN/PORTFOLIO/blob/main/.github/workflows/laboratory-image.yml) | GitHub Actions workflow for API tests, image build, Trivy vulnerability gate, CycloneDX SBOM, GHCR publication, and digest output | **Workflow source included** — remote registry publication has not been verified |
| [Argo CD GitOps Application](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/laboratory/deploy/gitops) | Argo CD Application tracking the Helm chart with automated sync, prune, self-heal, and content-digest image pinning support | **Source-ready** — no live Argo CD sync claimed |
| [Backstage Platform Starter](https://github.com/MD-SH0HAN/PORTFOLIO/tree/main/projects/platform/backstage) | Catalog Group/Component/API entities, a Python-service Scaffolder template, and a service skeleton with tests and CI workflow | **Starter source included** — no running Backstage installation or live template execution claimed |
| [Portfolio Website](https://github.com/MD-SH0HAN/PORTFOLIO) | Responsive static site, accessible navigation, project case studies, architecture explanations, and clearly labelled synthetic demonstrations | **Built static website** |

## Technology Toolkit

The tools below are grouped by the evidence in my repositories. A badge indicates that a technology appears in my work or learning path; it does **not** claim equal proficiency or professional production experience.

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

### Infrastructure and platform source included

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

These tools have corresponding source files, configurations, or workflows in the portfolio. Tool-dependent commands and live deployment still need to be run in an appropriately configured environment.

### Foundations I'm continuing to develop

<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />
  <img src="https://img.shields.io/badge/Networking-TCP%2FIP-00599C?style=flat-square" alt="Networking" />
  <img src="https://img.shields.io/badge/IAM_&_Cloud_Security-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="IAM and Cloud Security" />
  <img src="https://img.shields.io/badge/SRE_&_Reliability-44546A?style=flat-square" alt="SRE and reliability" />
  <img src="https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white" alt="OpenTelemetry" />
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible" />
</p>

## Engineering Principles

| Principle | How I apply it |
|---|---|
| **Infrastructure as Code** | Keep infrastructure definitions reviewable, repeatable, and separated by environment. |
| **Secure Defaults** | Prefer least privilege, non-root workloads, restricted capabilities, explicit network boundaries, and secret-safe workflows. |
| **Automation with Feedback** | Validate changes in CI and make failures, logs, and next steps understandable. |
| **GitOps and Traceability** | Keep desired deployment state version-controlled and use immutable image references for reviewed releases. |
| **Observability and Reliability** | Use metrics, health checks, alerts, and tests to understand service behavior and failure recovery. |
| **Platform as a Product** | Design templates and self-service workflows around developer needs, usability, ownership, and feedback. |
| **Cost Awareness** | Treat cloud cost, resource limits, and safe cleanup as part of infrastructure design. |
| **Honest Engineering Evidence** | Distinguish tested behavior, source-ready configuration, simulations, and actual deployments. |

## Current Learning Direction

My learning sequence is intentionally broad before it becomes specialized:

1. **Systems foundations:** Linux, operating systems, networking, DNS, TLS, Git, Python, and Bash.
2. **Cloud and infrastructure:** AWS networking and IAM, Terraform modules/state, security boundaries, and cost-aware resource design.
3. **Containers and orchestration:** Docker, Kubernetes workloads, probes, resource management, RBAC, NetworkPolicy, and Helm.
4. **Delivery and GitOps:** CI validation, image scanning, SBOMs, immutable image references, GitHub Actions, and Argo CD.
5. **Observability and SRE:** metrics, logs, traces, alert testing, SLIs/SLOs, incident response, and recovery exercises.
6. **Developer platforms:** Backstage catalog, software templates, documentation, golden paths, and self-service workflows.
7. **Operational maturity:** cloud security, policy as code, FinOps, disaster recovery, and safe AI-assisted infrastructure workflows.

I focus on learning a small set of complementary tools deeply instead of collecting badges for every product in the ecosystem.

## Validation Snapshot

**Portfolio source validation — 8 November 2026:**

- 24 in-memory Chromium browser checks passed across nine viewport widths and both themes.
- 12 observability API and smoke-script tests passed.
- 4 Backstage service-skeleton tests passed.
- Static HTML/CSS/JavaScript, infrastructure source-contract, standalone YAML, and workflow shell checks passed.

**Environment limitation:** Docker Compose live integration, Terraform CLI validation, Helm rendering, Kubernetes application, AWS provisioning, GHCR publication, Argo CD synchronization, and live Backstage scaffolding were not executed in that packaging environment. See the [portfolio validation report](https://github.com/MD-SH0HAN/PORTFOLIO/blob/main/VALIDATION_RESULTS.md) for the exact scope. These checks must be run in the relevant tools or deployment environment before claiming a live release.

## GitHub Contribution Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MD-SH0HAN/MD-SH0HAN/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MD-SH0HAN/MD-SH0HAN/output/github-contribution-grid-snake.svg" />
    <img src="https://raw.githubusercontent.com/MD-SH0HAN/MD-SH0HAN/output/github-contribution-grid-snake.svg" alt="GitHub contribution activity for MD Shohan" width="100%" />
  </picture>
</p>

## GitHub Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./profile/stats-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./profile/stats-light.svg" />
    <img src="./profile/stats-light.svg" alt="GitHub statistics for MD Shohan" height="180" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./profile/top-langs-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./profile/top-langs-light.svg" />
    <img src="./profile/top-langs-light.svg" alt="Most-used programming languages" height="180" />
  </picture>
</p>

<p align="center">
  <em>Learn deliberately. Build reproducibly. Operate responsibly. Make developers more effective.</em>
</p>

## Connect

<p align="center">
  <a href="https://md-sh0han.github.io/PORTFOLIO/"><img src="https://img.shields.io/badge/Portfolio-Visit-0A101F?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Visit my portfolio" /></a>
  &nbsp;
  <a href="https://github.com/MD-SH0HAN"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="Follow on GitHub" /></a>
  &nbsp;
  <a href="mailto:mohammad.and.shohan@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Contact by email" /></a>
</p>

<p align="center">
  <a href="https://www.facebook.com/mohammad.and.shohan" title="Facebook"><img src="https://cdn.simpleicons.org/facebook/0866FF" width="36" height="36" alt="Facebook" /></a>
  &nbsp;&nbsp;
  <a href="https://www.instagram.com/_md.shohan_/" title="Instagram"><img src="https://cdn.simpleicons.org/instagram/E4405F" width="36" height="36" alt="Instagram" /></a>
  &nbsp;&nbsp;
  <a href="https://www.threads.com/@_md.shohan_" title="Threads"><img src="https://cdn.simpleicons.org/threads/8B8B8B" width="36" height="36" alt="Threads" /></a>
  &nbsp;&nbsp;
  <a href="https://www.twitch.tv/md_shohan" title="Twitch"><img src="https://cdn.simpleicons.org/twitch/9146FF" width="36" height="36" alt="Twitch" /></a>
  &nbsp;&nbsp;
  <a href="https://www.tumblr.com/md-shohan" title="Tumblr"><img src="https://cdn.simpleicons.org/tumblr/36465D" width="36" height="36" alt="Tumblr" /></a>
  &nbsp;&nbsp;
  <a href="https://www.reddit.com/user/MD-SH0HAN/" title="Reddit"><img src="https://cdn.simpleicons.org/reddit/FF4500" width="36" height="36" alt="Reddit" /></a>
  &nbsp;&nbsp;
  <a href="https://vercel.com/md-shohan" title="Vercel"><img src="https://cdn.simpleicons.org/vercel/000000" width="36" height="36" alt="Vercel" /></a>
  &nbsp;&nbsp;
  <a href="https://gitlab.com/MD-SHOHAN" title="GitLab"><img src="https://cdn.simpleicons.org/gitlab/FC6D26" width="36" height="36" alt="GitLab" /></a>
  &nbsp;&nbsp;
  <a href="https://discord.com/users/1221600292915773468" title="Discord"><img src="https://cdn.simpleicons.org/discord/5865F2" width="36" height="36" alt="Discord" /></a>
  &nbsp;&nbsp;
  <a href="https://hub.docker.com/u/mdsh0han" title="Docker Hub"><img src="https://cdn.simpleicons.org/docker/2496ED" width="36" height="36" alt="Docker Hub" /></a>
</p>
