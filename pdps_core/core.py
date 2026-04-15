"""
Core framework implementation for PDPS-Core.
"""

from typing import Dict, List, Optional
from .personas import YunusPersona, YusufPersona, MusaPersona


class PDPSFramework:
    """
    Persona-Driven Problem Solving Framework
    
    Main class that orchestrates the three phases:
    1. Yunus (Accountability)
    2. Yusuf (Future Planning)
    3. Musa (System Understanding)
    """
    
    def __init__(self):
        self.yunus = YunusPersona()
        self.yusuf = YusufPersona()
        self.musa = MusaPersona()
        self.execution_history = []
    
    def run_pre_flight_check(self, context: Dict) -> Dict:
        """
        Run the pre-flight checklist for all three personas.
        
        Args:
            context: Dictionary containing problem/project context
        
        Returns:
            Dictionary with checklist results for each persona
        """
        results = {
            "yunus_check": self.yunus.get_checklist(),
            "yusuf_check": self.yusuf.get_checklist(),
            "musa_check": self.musa.get_checklist(),
            "overall_ready": False
        }
        
        # Check if all checklists are acknowledged (simplified)
        # In a real implementation, this would track user responses
        results["overall_ready"] = True
        
        return results
    
    def execute_phase(self, phase: str, context: Dict) -> Dict:
        """
        Execute a specific phase.
        
        Args:
            phase: One of 'yunus', 'yusuf', 'musa'
            context: Dictionary containing problem/project context
        
        Returns:
            Dictionary with execution results
        """
        phase_map = {
            "yunus": self.yunus,
            "yusuf": self.yusuf,
            "musa": self.musa
        }
        
        if phase not in phase_map:
            raise ValueError(f"Invalid phase: {phase}. Must be one of: yunus, yusuf, musa")
        
        persona = phase_map[phase]
        result = persona.execute(context)
        
        self.execution_history.append({
            "phase": phase,
            "timestamp": result.get("timestamp"),
            "result": result
        })
        
        return result
    
    def execute_all_phases(self, context: Dict) -> Dict:
        """
        Execute all three phases in sequence.
        
        Args:
            context: Dictionary containing problem/project context
        
        Returns:
            Dictionary with combined results from all phases
        """
        results = {
            "yunus": self.execute_phase("yunus", context),
            "yusuf": self.execute_phase("yusuf", context),
            "musa": self.execute_phase("musa", context),
            "summary": {}
        }
        
        # Generate summary
        results["summary"] = self._generate_summary(results)
        
        return results
    
    def _generate_summary(self, results: Dict) -> Dict:
        """Generate a summary of all phase executions."""
        summary = {
            "total_action_items": [],
            "critical_issues": [],
            "readiness_score": 0
        }
        
        # Collect action items from all phases
        for phase in ["yunus", "yusuf", "musa"]:
            action_items = results[phase].get("action_items", [])
            summary["total_action_items"].extend(action_items)
        
        # Calculate readiness score (simplified)
        yunus_accountability = results["yunus"].get("accountability_level", 0)
        yusuf_future = results["yusuf"].get("future_orientation", 0)
        yusuf_practical = results["yusuf"].get("practicality_score", 0)
        musa_system = results["musa"].get("system_knowledge", 0)
        musa_tech = results["musa"].get("technical_proficiency", 0)
        musa_balance = results["musa"].get("balance_score", 0)
        
        max_score = 3 + 5 + 5 + 5 + 10 + 5  # Maximum possible scores
        actual_score = yunus_accountability + yusuf_future + yusuf_practical + musa_system + musa_tech + musa_balance
        summary["readiness_score"] = min(100, int((actual_score / max_score) * 100))
        
        # Identify critical issues
        if yunus_accountability < 2:
            summary["critical_issues"].append("Dışaştırma sorunu devam ediyor - Yunus fazı tekrar edilmeli")
        if yusuf_future < 3 or yusuf_practical < 3:
            summary["critical_issues"].append("Gelecek odaklılık veya pratiklik eksik - Yusuf fazı güçlendirilmeli")
        if musa_system < 3 or musa_tech < 2:
            summary["critical_issues"].append("Sistem bilgisi veya teknik beceri yetersiz - Musa fazı çalışılmalı")
        
        return summary
    
    def get_execution_history(self) -> List[Dict]:
        """Get the history of all phase executions."""
        return self.execution_history
    
    def reset(self):
        """Reset the framework state."""
        self.execution_history = []
        self.yunus = YunusPersona()
        self.yusuf = YusufPersona()
        self.musa = MusaPersona()
