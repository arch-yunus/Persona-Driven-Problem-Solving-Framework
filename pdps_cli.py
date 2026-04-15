#!/usr/bin/env python3
"""
PDPS-Core CLI Tool
Persona-Driven Problem Solving Framework Command Line Interface
"""

import argparse
import json
import sys
from pdps_core import PDPSFramework


def print_banner():
    """Print the PDPS-Core banner."""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║          PDPS-Core: Persona-Driven Problem Solving            ║
║                    Framework CLI v0.1.0                       ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def run_checklist(args):
    """Run the pre-flight checklist."""
    framework = PDPSFramework()
    
    context = {
        "problem": args.problem or "",
        "project": args.project or "",
        "target_year": args.target_year or 2030,
        "system": args.system or "",
        "technical_skills": args.technical_skills or []
    }
    
    print("\n📋 Pre-Flight Checklist Running...\n")
    results = framework.run_pre_flight_check(context)
    
    print("=" * 60)
    print("YUNUS CHECK (System Debug & Accountability)")
    print("=" * 60)
    for i, item in enumerate(results["yunus_check"], 1):
        print(f"  [ ] {item}")
    
    print("\n" + "=" * 60)
    print("YUSUF CHECK (Predictive Architecture & Field Execution)")
    print("=" * 60)
    for i, item in enumerate(results["yusuf_check"], 1):
        print(f"  [ ] {item}")
    
    print("\n" + "=" * 60)
    print("MUSA CHECK (System Penetration & Balanced Methodology)")
    print("=" * 60)
    for i, item in enumerate(results["musa_check"], 1):
        print(f"  [ ] {item}")
    
    print(f"\n✅ Overall Ready: {results['overall_ready']}")
    
    return results


def run_execute(args):
    """Execute all phases."""
    framework = PDPSFramework()
    
    context = {
        "problem": args.problem or "",
        "project": args.project or "",
        "target_year": args.target_year or 2030,
        "system": args.system or "",
        "technical_skills": args.technical_skills or []
    }
    
    print("\n🚀 Executing All PDPS Phases...\n")
    
    results = framework.execute_all_phases(context)
    
    # Print results for each phase
    for phase_name in ["yunus", "yusuf", "musa"]:
        phase_result = results[phase_name]
        print("=" * 60)
        print(f"{phase_name.upper()} PHASE RESULTS")
        print("=" * 60)
        print(f"Status: {phase_result['status']}")
        
        for key, value in phase_result.items():
            if key != "status" and key != "action_items":
                print(f"  {key}: {value}")
        
        if phase_result.get("action_items"):
            print("\n  Action Items:")
            for item in phase_result["action_items"]:
                print(f"    • {item}")
        
        print()
    
    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    summary = results["summary"]
    print(f"Readiness Score: {summary['readiness_score']}%")
    
    if summary["total_action_items"]:
        print("\nTotal Action Items:")
        for item in summary["total_action_items"]:
            print(f"  • {item}")
    
    if summary["critical_issues"]:
        print("\n⚠️  Critical Issues:")
        for issue in summary["critical_issues"]:
            print(f"  • {issue}")
    
    # Save to file if requested
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Results saved to: {args.output}")
    
    return results


def run_phase(args):
    """Execute a specific phase."""
    framework = PDPSFramework()
    
    context = {
        "problem": args.problem or "",
        "project": args.project or "",
        "target_year": args.target_year or 2030,
        "system": args.system or "",
        "technical_skills": args.technical_skills or []
    }
    
    print(f"\n🎯 Executing {args.phase.upper()} Phase...\n")
    
    result = framework.execute_phase(args.phase, context)
    
    print("=" * 60)
    print(f"{args.phase.upper()} PHASE RESULTS")
    print("=" * 60)
    print(f"Status: {result['status']}")
    
    for key, value in result.items():
        if key != "status" and key != "action_items":
            print(f"  {key}: {value}")
    
    if result.get("action_items"):
        print("\nAction Items:")
        for item in result["action_items"]:
            print(f"  • {item}")
    
    return result


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="PDPS-Core: Persona-Driven Problem Solving Framework CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run pre-flight checklist
  python pdps_cli.py checklist --problem "Project is failing due to external factors"
  
  # Execute all phases
  python pdps_cli.py execute --project "AI-powered agricultural system" --target-year 2030
  
  # Execute specific phase
  python pdps_cli.py phase --phase yunus --problem "Team blaming external factors"
  
  # Execute with system context
  python pdps_cli.py execute --system "Working in a large tech company" --technical_skills python data-science
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Checklist command
    checklist_parser = subparsers.add_parser("checklist", help="Run pre-flight checklist")
    checklist_parser.add_argument("--problem", type=str, help="Problem statement")
    checklist_parser.add_argument("--project", type=str, help="Project description")
    checklist_parser.add_argument("--target-year", type=int, help="Target year for future planning")
    checklist_parser.add_argument("--system", type=str, help="System context")
    checklist_parser.add_argument("--technical-skills", type=str, nargs="*", help="Technical skills")
    
    # Execute command
    execute_parser = subparsers.add_parser("execute", help="Execute all phases")
    execute_parser.add_argument("--problem", type=str, help="Problem statement")
    execute_parser.add_argument("--project", type=str, help="Project description")
    execute_parser.add_argument("--target-year", type=int, help="Target year for future planning")
    execute_parser.add_argument("--system", type=str, help="System context")
    execute_parser.add_argument("--technical-skills", type=str, nargs="*", help="Technical skills")
    execute_parser.add_argument("--output", type=str, help="Output JSON file path")
    
    # Phase command
    phase_parser = subparsers.add_parser("phase", help="Execute a specific phase")
    phase_parser.add_argument("--phase", type=str, required=True, choices=["yunus", "yusuf", "musa"], help="Phase to execute")
    phase_parser.add_argument("--problem", type=str, help="Problem statement")
    phase_parser.add_argument("--project", type=str, help="Project description")
    phase_parser.add_argument("--target-year", type=int, help="Target year for future planning")
    phase_parser.add_argument("--system", type=str, help="System context")
    phase_parser.add_argument("--technical-skills", type=str, nargs="*", help="Technical skills")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    print_banner()
    
    if args.command == "checklist":
        run_checklist(args)
    elif args.command == "execute":
        run_execute(args)
    elif args.command == "phase":
        run_phase(args)


if __name__ == "__main__":
    main()
