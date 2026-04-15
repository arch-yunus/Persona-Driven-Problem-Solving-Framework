# PDPS-Core Usage Guide

This guide provides practical examples of how to use the Persona-Driven Problem Solving Framework.

## Installation

```bash
# Clone the repository
git clone https://github.com/arch-yunus/Persona-Driven-Problem-Solving-Framework.git
cd Persona-Driven-Problem-Solving-Framework

# Install the package
pip install -e .
```

## Using the CLI Tool

### 1. Run Pre-Flight Checklist

Before starting any project, run the pre-flight checklist to ensure you're ready:

```bash
python pdps_cli.py checklist --problem "Project is failing due to external factors"
```

### 2. Execute All Phases

Run all three phases with your project context:

```bash
python pdps_cli.py execute \
  --project "AI-powered agricultural system" \
  --target-year 2030 \
  --system "Working in a large tech company" \
  --technical-skills python data-science machine-learning
```

### 3. Execute Specific Phase

Run a single phase when you need to focus on a specific aspect:

```bash
# Yunus phase (Accountability)
python pdps_cli.py phase --phase yunus --problem "Team blaming external factors"

# Yusuf phase (Future Planning)
python pdps_cli.py phase --phase yusuf --project "Blockchain-based supply chain" --target-year 2035

# Musa phase (System Understanding)
python pdps_cli.py phase --phase musa --system "Corporate banking infrastructure" --technical-skills python security
```

### 4. Save Results to File

Export execution results to JSON for documentation:

```bash
python pdps_cli.py execute \
  --project "Smart city infrastructure" \
  --output results.json
```

## Using as a Python Library

### Basic Usage

```python
from pdps_core import PDPSFramework

# Initialize the framework
framework = PDPSFramework()

# Define your context
context = {
    "problem": "Our startup is failing because of market conditions",
    "project": "AI-powered educational platform",
    "target_year": 2030,
    "system": "Silicon Valley startup ecosystem",
    "technical_skills": ["python", "machine-learning", "data-science"]
}

# Run all phases
results = framework.execute_all_phases(context)

# Print summary
print(f"Readiness Score: {results['summary']['readiness_score']}%")
print("Action Items:")
for item in results['summary']['total_action_items']:
    print(f"  - {item}")
```

### Running Individual Phases

```python
from pdps_core import PDPSFramework

framework = PDPSFramework()

# Run only Yunus phase
yunus_result = framework.execute_phase("yunus", {
    "problem": "Team keeps blaming external factors"
})

# Run only Yusuf phase
yusuf_result = framework.execute_phase("yusuf", {
    "project": "Renewable energy grid",
    "target_year": 2030
})

# Run only Musa phase
musa_result = framework.execute_phase("musa", {
    "system": "Government infrastructure",
    "technical_skills": ["python", "cybersecurity"]
})
```

### Pre-Flight Checklist

```python
from pdps_core import PDPSFramework

framework = PDPSFramework()

context = {
    "problem": "Project delays due to vendor issues",
    "project": "E-commerce platform",
    "target_year": 2025
}

checklist = framework.run_pre_flight_check(context)

print("Yunus Checklist:")
for item in checklist['yunus_check']:
    print(f"  [ ] {item}")

print("\nYusuf Checklist:")
for item in checklist['yusuf_check']:
    print(f"  [ ] {item}")

print("\nMusa Checklist:")
for item in checklist['musa_check']:
    print(f"  [ ] {item}")
```

## Practical Examples

### Example 1: Startup Crisis Management

```python
from pdps_core import PDPSFramework

framework = PDPSFramework()

context = {
    "problem": "Our startup is failing because investors pulled out and the market is tough",
    "project": "AI-powered healthcare diagnostics",
    "target_year": 2030,
    "system": "Healthcare startup ecosystem",
    "technical_skills": ["python", "machine-learning", "healthcare-it"]
}

results = framework.execute_all_phases(context)

# Review the results
if results['yunus']['accountability_level'] < 2:
    print("⚠️  You're still externalizing blame. Focus on what you can control.")

if results['yusuf']['future_orientation'] < 3:
    print("⚠️  Project needs more focus on future problems (2030+ AI era).")

if results['musa']['technical_proficiency'] < 2:
    print("⚠️  Need to strengthen technical skills to compete in the system.")
```

### Example 2: Corporate Innovation Project

```python
from pdps_core import PDPSFramework

framework = PDPSFramework()

context = {
    "problem": "Innovation team stuck in bureaucratic processes",
    "project": "Digital transformation initiative",
    "target_year": 2025,
    "system": "Large enterprise with legacy systems",
    "technical_skills": ["java", "cloud-computing", "devops"]
}

results = framework.execute_all_phases(context)

# Get actionable insights
print("Action Items:")
for item in results['summary']['total_action_items']:
    print(f"• {item}")
```

### Example 3: Personal Development

```python
from pdps_core import PDPSFramework

framework = PDPSFramework()

context = {
    "problem": "Career stagnation despite hard work",
    "project": "Skill development in AI engineering",
    "target_year": 2026,
    "system": "Tech industry job market",
    "technical_skills": ["python", "data-science"]
}

results = framework.execute_all_phases(context)

# Track your progress
readiness = results['summary']['readiness_score']
print(f"Your readiness score: {readiness}%")

if readiness < 50:
    print("Focus on improving the areas highlighted in critical issues.")
else:
    print("You're on the right track! Continue executing the action items.")
```

## Integration with Project Management

You can integrate PDPS-Core into your existing project management workflow:

```python
# In your project initialization script
from pdps_core import PDPSFramework

def initialize_project(project_name, context):
    framework = PDPSFramework()
    
    # Run pre-flight check
    checklist = framework.run_pre_flight_check(context)
    
    # If not ready, provide guidance
    if not checklist['overall_ready']:
        print("Project not ready. Review checklists above.")
        return False
    
    # Execute all phases
    results = framework.execute_all_phases(context)
    
    # Save results for project documentation
    save_to_project_file(project_name, results)
    
    return True

# Usage
initialize_project("AI-Agriculture", {
    "project": "AI-powered agricultural optimization",
    "target_year": 2030,
    "system": "AgriTech startup ecosystem",
    "technical_skills": ["python", "machine-learning", "iot"]
})
```

## Best Practices

1. **Always run the pre-flight checklist** before starting any major initiative
2. **Be honest in your context inputs** - the framework works best with accurate self-assessment
3. **Review action items regularly** - they should guide your strategic decisions
4. **Re-run phases periodically** - as your context changes, so should your approach
5. **Use the readiness score** as a metric for your strategic alignment

## Troubleshooting

### Low Readiness Score

If your readiness score is below 50%, focus on:
- Improving accountability (Yunus phase)
- Enhancing future orientation (Yusuf phase)
- Strengthening system knowledge and technical skills (Musa phase)

### External Blame Patterns

If the Yunus phase detects external blame patterns:
- Reflect on what you can control
- Accept responsibility for your role in the situation
- Focus on actionable solutions rather than complaints

### Lack of Future Orientation

If the Yusuf phase shows low future orientation:
- Research emerging trends in your field
- Consider long-term implications (5-10 years)
- Design solutions for future problems, not current ones

### Insufficient System Knowledge

If the Musa phase shows low system knowledge:
- Study the systems you're working within
- Develop technical skills relevant to your domain
- Understand both the material and philosophical aspects of your field
