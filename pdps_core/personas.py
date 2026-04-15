"""
Persona classes for the PDPS-Core framework.
Each persona represents a phase of problem-solving.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from datetime import datetime


class Persona(ABC):
    """Base class for all personas."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.checklist = []
        self.reflections = []
    
    @abstractmethod
    def execute(self, context: Dict) -> Dict:
        """Execute the persona's algorithm with given context."""
        pass
    
    @abstractmethod
    def get_checklist(self) -> List[str]:
        """Get the pre-flight checklist for this persona."""
        pass
    
    def add_reflection(self, reflection: str):
        """Add a reflection note."""
        self.reflections.append({
            "timestamp": datetime.now().isoformat(),
            "content": reflection
        })
    
    def get_reflections(self) -> List[Dict]:
        """Get all reflections."""
        return self.reflections


class YunusPersona(Persona):
    """
    Phase 1: Yunus Persona (System Debug & Accountability)
    
    Focus: Confrontation and Big Picture
    Problem: When we make mistakes or get "swallowed" by the worldly (fish), 
    we insist on blaming others.
    Algorithm:
    1. Remember the big picture (Tawhid)
    2. Stop externalizing and confront your own "bug" in the system
    3. Take responsibility: "I was indeed among the wrongdoers"
    """
    
    def __init__(self):
        super().__init__(
            name="Yunus",
            description="System Debug & Accountability - Face the truth and take responsibility"
        )
    
    def execute(self, context: Dict) -> Dict:
        """Execute Yunus persona algorithm."""
        result = {
            "phase": "Yunus",
            "status": "in_progress",
            "accountability_level": 0,
            "external_blame_detected": [],
            "action_items": []
        }
        
        # Check for external blame patterns
        problem_statement = context.get("problem", "")
        blame_patterns = ["sistemin suçu", "onların hatası", "zalimlerin", "dış güçler"]
        
        for pattern in blame_patterns:
            if pattern.lower() in problem_statement.lower():
                result["external_blame_detected"].append(pattern)
        
        # Generate action items based on accountability check
        if result["external_blame_detected"]:
            result["action_items"].append(
                "Dışaştırma durdur: Sorunun kendi payını kabul et"
            )
            result["accountability_level"] = 1
        else:
            result["accountability_level"] = 3
            result["action_items"].append(
                "Sorumluluk alındı: Sistemi sıfırla ve net zihinle devam et"
            )
        
        result["status"] = "completed"
        return result
    
    def get_checklist(self) -> List[str]:
        """Get Yunus pre-flight checklist."""
        return [
            "Bu krizde/problemde benim veya benim mahallemin payı ne?",
            "Kendi kusurumu tamamen kabul edip sistemi sıfırladım mı?",
            "Büyük resmi (Tevhidi) hatırladım mı?",
            "Dışaştırma yapmayı bıraktım mı?"
        ]


class YusufPersona(Persona):
    """
    Phase 2: Yusuf Persona (Predictive Architecture & Field Execution)
    
    Focus: Predicting the Future and Entering the Field
    Problem: Doing the same fractional/sectarian debates for hundreds of years 
    and confining religion/morality concepts only to "theology" (theoretical level)
    Algorithm:
    1. Turn your face to the future, not the past
    2. Predict the future's problem with revelation and reason (science)
    3. Put on your work clothes and enter the most "secular" looking field
    4. Execute Imam Malik's rule: "Nakil is not science" - design practical, 
       touchable architectures to solve the problem of time
    """
    
    def __init__(self):
        super().__init__(
            name="Yusuf",
            description="Predictive Architecture & Field Execution - Predict future and implement practically"
        )
    
    def execute(self, context: Dict) -> Dict:
        """Execute Yusuf persona algorithm."""
        result = {
            "phase": "Yusuf",
            "status": "in_progress",
            "future_orientation": 0,
            "practicality_score": 0,
            "action_items": []
        }
        
        project_description = context.get("project", "")
        target_year = context.get("target_year", 2030)
        
        # Check if project is future-oriented
        future_keywords = ["yapay zeka", "ai", "2030", "gelecek", "yeni teknoloji", "digital"]
        future_score = sum(1 for kw in future_keywords if kw.lower() in project_description.lower())
        result["future_orientation"] = min(future_score, 5)
        
        # Check practical implementation
        practical_keywords = ["uygulama", "kod", "sistem", "mimari", "pratik", "implementasyon"]
        practical_score = sum(1 for kw in practical_keywords if kw.lower() in project_description.lower())
        result["practicality_score"] = min(practical_score, 5)
        
        # Generate action items
        if result["future_orientation"] < 3:
            result["action_items"].append(
                f"Geleceğe dön: {target_year}ların sorunlarına odaklan"
            )
        
        if result["practicality_score"] < 3:
            result["action_items"].append(
                "Sahaya in: Teorik tartışma yerine pratik mimariler tasarla"
            )
        
        if result["future_orientation"] >= 3 and result["practicality_score"] >= 3:
            result["action_items"].append(
                "İzleri giy ve sahaya in: Zamanın problemini çözen mimari hazır"
            )
        
        result["status"] = "completed"
        return result
    
    def get_checklist(self) -> List[str]:
        """Get Yusuf pre-flight checklist."""
        return [
            "Bu proje geçmiş yüzyılların tartışmalarına mı cevap veriyor, "
            "yoksa 2030'ların (Yapay Genel Zeka dönemi) sorunlarını mı çözüyor?",
            "İzleri giyip sahaya (pratiğe) inmeye hazır mıyım?",
            "Zamanın problemini çözecek pratik, dokunulabilir mimariler tasladım mı?"
        ]


class MusaPersona(Persona):
    """
    Phase 3: Musa Persona (System Penetration & Balanced Methodology)
    
    Focus: Knowing the System from Inside and Uniting Two Seas
    Problem: Oscillating between idealism (going to the mountain and completely 
    disconnecting from the system) and realism (melting inside the system, 
    i.e., assimilating into Pharaoh's)
    Algorithm:
    1. Know the system from inside
    2. Take "Time's Staff" (Data, Coding, Engineering) in hand
    3. Don't settle for material knowledge only, move towards 
       "where two seas (Reason and Revelation) meet"
    """
    
    def __init__(self):
        super().__init__(
            name="Musa",
            description="System Penetration & Balanced Methodology - Know system and balance reason with revelation"
        )
    
    def execute(self, context: Dict) -> Dict:
        """Execute Musa persona algorithm."""
        result = {
            "phase": "Musa",
            "status": "in_progress",
            "system_knowledge": 0,
            "technical_proficiency": 0,
            "balance_score": 0,
            "action_items": []
        }
        
        system_context = context.get("system", "")
        technical_skills = context.get("technical_skills", [])
        
        # Check system knowledge
        system_keywords = ["sistem", "yapı", "mekanizma", "işleyiş", "altyapı"]
        system_score = sum(1 for kw in system_keywords if kw.lower() in system_context.lower())
        result["system_knowledge"] = min(system_score, 5)
        
        # Check technical proficiency
        result["technical_proficiency"] = len(technical_skills)
        
        # Check balance (reason + revelation)
        balance_keywords = ["akıl", "vahiy", "bilim", "din", "dengeli", "orta yol"]
        balance_score = sum(1 for kw in balance_keywords if kw.lower() in system_context.lower())
        result["balance_score"] = min(balance_score, 5)
        
        # Generate action items
        if result["system_knowledge"] < 3:
            result["action_items"].append(
                "Sistemi içinden tanı: Firavun'un sarayında büyü"
            )
        
        if result["technical_proficiency"] < 2:
            result["action_items"].append(
                "Zamanın Asasını al: Data, Kodlama, Mühendislik becerilerini geliştir"
            )
        
        if result["balance_score"] < 3:
            result["action_items"].append(
                "İki Denizin buluştuğu yere doğru yola çık: Akıl ve Vahiy dengesi"
            )
        
        if result["system_knowledge"] >= 3 and result["technical_proficiency"] >= 2 and result["balance_score"] >= 3:
            result["action_items"].append(
                "Zamanın Asası elinde: Sistemi içinden dönüştürmeye hazır"
            )
        
        result["status"] = "completed"
        return result
    
    def get_checklist(self) -> List[str]:
        """Get Musa pre-flight checklist."""
        return [
            "Karşındaki gücün (teknoloji tekelleri, konformizm) altyapısını yeterince iyi tanıyor muyum?",
            "Elimde onların sihirbazlarını (Amon Rahiplerini) yutacak 'Zamanın Asası' "
            "(teknik donanım ve usul) var mı?",
            "İki Denizin (Akıl ve Vahyin) buluştuğu yere doğru yola çıktım mı?"
        ]
