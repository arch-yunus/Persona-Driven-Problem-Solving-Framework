"""
Startup crisis management example for PDPS-Core
"""

from pdps_core import PDPSFramework


def main():
    """Demonstrate PDPS framework for startup crisis management."""
    
    framework = PDPSFramework()
    
    # Startup crisis context
    context = {
        "problem": "Our startup is failing because investors pulled out, the market is saturated, and competitors are unfair",
        "project": "AI-powered healthcare diagnostics platform",
        "target_year": 2030,
        "system": "Healthcare startup ecosystem with heavy regulation",
        "technical_skills": ["python", "machine-learning", "healthcare-it", "data-privacy"]
    }
    
    print("=" * 60)
    print("Startup Crisis Management - PDPS-Core")
    print("=" * 60)
    
    # Execute all phases
    results = framework.execute_all_phases(context)
    
    # Analyze Yunus phase (Accountability)
    print("\n" + "=" * 60)
    print("PHASE 1: YUNUS - Accountability Analysis")
    print("=" * 60)
    
    yunus = results['yunus']
    print(f"Accountability Level: {yunus['accountability_level']}/3")
    
    if yunus['external_blame_detected']:
        print("\n⚠️  External blame patterns detected:")
        for pattern in yunus['external_blame_detected']:
            print(f"  - '{pattern}'")
        print("\nRecommendation: Stop externalizing. Focus on what you can control.")
    
    # Analyze Yusuf phase (Future Planning)
    print("\n" + "=" * 60)
    print("PHASE 2: YUSUF - Future Planning Analysis")
    print("=" * 60)
    
    yusuf = results['yusuf']
    print(f"Future Orientation: {yusuf['future_orientation']}/5")
    print(f"Practicality Score: {yusuf['practicality_score']}/5")
    
    if yusuf['future_orientation'] < 3:
        print("\n⚠️  Low future orientation. Consider:")
        print("  - AI's impact on healthcare by 2030")
        print("  - Regulatory changes in medical AI")
        print("  - Telemedicine and remote diagnostics trends")
    
    # Analyze Musa phase (System Understanding)
    print("\n" + "=" * 60)
    print("PHASE 3: MUSA - System Understanding Analysis")
    print("=" * 60)
    
    musa = results['musa']
    print(f"System Knowledge: {musa['system_knowledge']}/5")
    print(f"Technical Proficiency: {musa['technical_proficiency']}/10")
    print(f"Balance Score: {musa['balance_score']}/5")
    
    if musa['technical_proficiency'] < 3:
        print("\n⚠️  Need to strengthen technical skills:")
        print("  - Deep learning for medical imaging")
        print("  - HIPAA compliance and data security")
        print("  - Clinical workflow integration")
    
    # Overall assessment
    print("\n" + "=" * 60)
    print("OVERALL ASSESSMENT")
    print("=" * 60)
    
    readiness = results['summary']['readiness_score']
    print(f"Strategic Readiness: {readiness}%")
    
    if readiness < 40:
        print("\n🔴 Critical: Major gaps in strategic approach")
    elif readiness < 70:
        print("\n🟡 Warning: Some areas need improvement")
    else:
        print("\n🟢 Good: Strong strategic alignment")
    
    print("\nRecommended Actions:")
    for item in results['summary']['total_action_items']:
        print(f"  • {item}")
    
    if results['summary']['critical_issues']:
        print("\nCritical Issues to Address:")
        for issue in results['summary']['critical_issues']:
            print(f"  ⚠️  {issue}")


if __name__ == "__main__":
    main()
