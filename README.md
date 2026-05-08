SSDD Project – Secure System for Detection and Defense

Project Overview
The SSDD Project is a Flask-based cybersecurity application developed to demonstrate secure software development practices and cybersecurity testing methodologies. The system focuses on detecting malicious or adversarial inputs using machine learning-based analysis and integrates both Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST).

The project simulates real-world cybersecurity scenarios by testing applications against different attack patterns and vulnerabilities while maintaining a collaborative GitHub development workflow.



Features
- Flask-based web application
- Machine learning-based attack analysis
- FGSM adversarial attack simulation
- Static Application Security Testing (SAST)
- Dynamic Application Security Testing (DAST)
- Real-time input testing
- Collaborative GitHub workflow and branch management



SAST Implementation
Static Application Security Testing (SAST) was implemented using Bandit to analyze the source code for potential security vulnerabilities before runtime.

Tool Used
- Bandit (Python Security Scanner)

Purpose
The SAST module was used to:
- identify insecure coding practices
- detect unsafe functions
- improve application security
- analyze source code vulnerabilities

command Used
```bash
bandit -r .
```

---

DAST Implementation
Dynamic Application Security Testing (DAST) was performed on the running Flask application to evaluate runtime security behavior and test the system against malicious inputs.

Methods Used
- Manual attack payload testing
- Runtime input validation
- Web application security testing

 Attacks Tested
- SQL Injection
- Cross-Site Scripting (XSS)
- Malicious input payloads
- Adversarial attack simulation

## Example Payloads
```json
{
  "Input": "' OR 1=1 --"
}
```

```json
{
  "Input": "<script>alert(1)</script>"
}
```

---

 Technologies Used
- Python
- Flask
- Machine Learning
- GitHub
- Bandit
- HTML/CSS
- Cybersecurity Testing Concepts

---

GitHub Workflow
The project was developed collaboratively using GitHub branches and merge-based workflow management.

## Development Branches
- `feature-sast-main`
- `feature-dast-testing`
- `attacks`
- `main`

The workflow included:
- branch creation
- feature development
- repository collaboration
- commit management
- merge handling
- final integration and project supervision

---

 Team Contributions

 Alishba Mir – Repository Owner & Project Lead
- Supervised complete project workflow
- Managed GitHub repository
- Reviewed and merged branches
- Coordinated project integration and finalization
- Managed final project structure and submission preparation

 Maliha Imran – SAST Module Development
- Worked on SAST implementation
- Assisted in static security testing integration
- Contributed to vulnerability analysis and testing

Noor Ul Ain – DAST Testing Module
- Worked on DAST implementation and runtime testing
- Assisted in attack payload testing
- Contributed to dynamic security testing concepts

Qurat Ul Ain – Repository Collaboration & Integration
- Assisted in merge operations and repository synchronization
- Participated in collaborative development workflow
- Helped maintain project consistency during integration

 Aman Kaleem – Attack Simulation & Development
- Worked on attack simulation features
- Assisted in adversarial testing implementation
- Contributed to attack-related functionality and testing
ence in secure software development, vulnerability analysis, cybersecurity testing, and collaborative project management. The integration of SAST, DAST, and adversarial attack simulation demonstrates the importance of proactive security testing in modern software systems.
