"""
Basic usage example for PDPS-Core
"""

from pdps_core import PDPSFramework


def main():
    """Demonstrate basic usage of the PDPS framework."""
    
    # Initialize the framework
    framework = PDPSFramework()
    
    # Define your context
    context = {
        "problem": "Our project is delayed because of external dependencies",
        "project": "AI-powered educational platform for 2030",
        "target_year": 2030,
        "system": "EdTech startup ecosystem",
        "technical_skills": ["python", "machine-learning", "data-science"]
    }
    
    print("=" * 60)
    print("PDPS-Core Basic Usage Example")
    print("=" * 60)
    
    # Run pre-flight checklist
    print("\n1. Running Pre-Flight Checklist...")
    checklist = framework.run_pre_flight_check(context)
    
    print("\nYunus Checklist:")
    for item in checklist['yunus_check']:
        print(f"  [ ] {item}")
    
    print("\nYusuf Checklist:")
    for item in checklist['yusuf_check']:
        print(f"  [ ] {item}")
    
    print("\nMusa Checklist:")
    for item in checklist['musa_check']:
        print(f"  [ ] {item}")
    
    # Execute all phases
    print("\n2. Executing All Phases...")
    results = framework.execute_all_phases(context)
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    print(f"\nReadiness Score: {results['summary']['readiness_score']}%")
    
    if results['summary']['total_action_items']:
        print("\nAction Items:")
        for item in results['summary']['total_action_items']:
            print(f"  • {item}")
    
    if results['summary']['critical_issues']:
        print("\nCritical Issues:")
        for issue in results['summary']['critical_issues']:
            print(f"  ⚠️  {issue}")
    
    # Display phase-specific results
    for phase_name in ["yunus", "yusuf", "musa"]:
        phase_result = results[phase_name]
        print(f"\n{phase_name.upper()} Phase:")
        print(f"  Status: {phase_result['status']}")
        if phase_result.get('action_items'):
            print("  Actions:")
            for action in phase_result['action_items']:
                print(f"    - {action}")


if __name__ == "__main__":
    main()
