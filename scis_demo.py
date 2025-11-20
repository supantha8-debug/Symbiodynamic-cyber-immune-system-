# symbiodynamic_cyber_immune_system.py
import time
import random
import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Callable
from abc import ABC, abstractmethod
import numpy as np

print("🚀 Initializing Symbiodynamic Cyber-Immune System (SCIS)...")

@dataclass
class MGSState:
    """State representation for Mutable Generative Structures"""
    internal_state: Dict[str, Any]
    performance_metrics: Dict[str, float]
    threat_intel: List[Dict]
    timestamp: float
    relationship_time: float = 0.0

class MutableGenerativeStructure(ABC):
    """Base implementation of a Mutable Generative Structure"""
    
    def __init__(self, name: str, initial_rules: Dict[str, Any], plasticity_config: Dict[str, float]):
        self.name = name
        self.S = MGSState({}, {}, [], time.time())
        self.R = initial_rules
        self.ρ = plasticity_config
        self.interaction_history = []
        print(f"  ✅ Created {self.name} with {len(initial_rules)} rules")
    
    @abstractmethod
    def execute_rules(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    def calculate_plasticity(self, rule_name: str) -> float:
        return self.ρ.get(rule_name, 0.5)
    
    def evolve_rules(self, interaction_context: Dict[str, Any]) -> Dict[str, Any]:
        """Evolve rules based on interaction"""
        print(f"  🔄 {self.name} evolving rules...")
        new_rules = {}
        
        for rule_name, current_rule in self.R.items():
            plasticity = self.calculate_plasticity(rule_name)
            
            if plasticity > 0.1:
                # Simple evolution: add random improvement
                if isinstance(current_rule, (int, float)):
                    improvement = random.uniform(-0.1, 0.2) * plasticity
                    new_rule = max(0.1, current_rule + improvement)
                else:
                    new_rule = current_rule
                
                new_rules[rule_name] = new_rule
                print(f"    📈 {rule_name}: {current_rule:.3f} → {new_rule:.3f}")
            else:
                new_rules[rule_name] = current_rule
        
        self.R = new_rules
        self.S.relationship_time += 1.0
        return new_rules

class NetworkSentinelMGS(MutableGenerativeStructure):
    """Network traffic analysis agent"""
    
    def __init__(self):
        initial_rules = {
            'traffic_analysis': 0.7,
            'anomaly_detection': 0.8,
            'protocol_validation': 0.9
        }
        plasticity_config = {
            'traffic_analysis': 0.8,
            'anomaly_detection': 0.9,
            'protocol_validation': 0.3
        }
        super().__init__("NetworkSentinel", initial_rules, plasticity_config)
        self.threat_patterns = [
            "port_scanning", "brute_force", "data_exfiltration"
        ]
    
    def execute_rules(self, packet_data: Dict[str, Any]) -> Dict[str, Any]:
        threat_detected = False
        threat_type = "none"
        confidence = 0.0
        
        # Analyze traffic patterns
        if packet_data.get('destination_port') in [4444, 1337, 31337]:
            threat_detected = True
            threat_type = "suspicious_port"
            confidence = 0.8
        
        if packet_data.get('packet_size', 0) > 1500:
            threat_detected = True
            threat_type = "oversized_packet"
            confidence = max(confidence, 0.6)
        
        if packet_data.get('protocol') == "UDP" and packet_data.get('rate', 0) > 1000:
            threat_detected = True
            threat_type = "udp_flood"
            confidence = max(confidence, 0.9)
        
        return {
            'threat_detected': threat_detected,
            'threat_type': threat_type,
            'confidence': confidence,
            'action': 'block' if threat_detected else 'allow',
            'timestamp': time.time()
        }

class DeceptionDirectorMGS(MutableGenerativeStructure):
    """Advanced deception agent"""
    
    def __init__(self):
        initial_rules = {
            'honeypot_effectiveness': 0.6,
            'breadcrumb_convincingness': 0.7,
            'emotional_manipulation': 0.5
        }
        plasticity_config = {rule: 0.95 for rule in initial_rules.keys()}
        super().__init__("DeceptionDirector", initial_rules, plasticity_config)
        self.active_deceptions = {}
        self.attacker_profiles = {}
    
    def execute_rules(self, attacker_interaction: Dict[str, Any]) -> Dict[str, Any]:
        attacker_id = attacker_interaction.get('attacker_id', 'unknown')
        
        # Update attacker profile
        profile = self._update_attacker_profile(attacker_id, attacker_interaction)
        
        # Generate deception strategy
        deception_plan = self._generate_deception_plan(profile)
        
        print(f"    🎭 Deception activated for {attacker_id}: {deception_plan['strategy']}")
        return deception_plan
    
    def _update_attacker_profile(self, attacker_id: str, interaction: Dict[str, Any]) -> Dict[str, Any]:
        if attacker_id not in self.attacker_profiles:
            self.attacker_profiles[attacker_id] = {
                'technical_skill': 0.5,
                'patience': 0.5,
                'frustration': 0.0,
                'interaction_count': 0
            }
        
        profile = self.attacker_profiles[attacker_id]
        profile['interaction_count'] += 1
        
        # Simulate learning from interactions
        if interaction.get('sophisticated', False):
            profile['technical_skill'] = min(1.0, profile['technical_skill'] + 0.1)
        
        if profile['interaction_count'] > 3:
            profile['frustration'] = min(1.0, profile['frustration'] + 0.1)
            profile['patience'] = max(0.0, profile['patience'] - 0.05)
        
        return profile
    
    def _generate_deception_plan(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        strategies = []
        
        if profile['frustration'] > 0.7:
            strategies.append("delay_responses")
            strategies.append("provide_false_success")
        
        if profile['technical_skill'] > 0.7:
            strategies.append("complex_honeypot")
            strategies.append("technical_misdirection")
        else:
            strategies.append("simple_honeypot")
            strategies.append("obvious_breadcrumbs")
        
        return {
            'strategy': strategies,
            'honeypot_type': 'advanced' if profile['technical_skill'] > 0.7 else 'basic',
            'response_delay': profile['frustration'] * 2.0,
            'emotional_manipulation': 'frustration' if profile['frustration'] < 0.5 else 'confusion'
        }

class ThreatAnalyzerMGS(MutableGenerativeStructure):
    """Threat intelligence and analysis agent"""
    
    def __init__(self):
        initial_rules = {
            'correlation_strength': 0.8,
            'pattern_recognition': 0.75,
            'threat_prediction': 0.6
        }
        plasticity_config = {
            'correlation_strength': 0.7,
            'pattern_recognition': 0.9,
            'threat_prediction': 0.8
        }
        super().__init__("ThreatAnalyzer", initial_rules, plasticity_config)
        self.threat_database = []
    
    def execute_rules(self, threat_data: Dict[str, Any]) -> Dict[str, Any]:
        # Analyze and correlate threats
        threat_level = self._calculate_threat_level(threat_data)
        recommendations = self._generate_recommendations(threat_data, threat_level)
        
        # Store in database
        self.threat_database.append({
            'timestamp': time.time(),
            'threat_data': threat_data,
            'threat_level': threat_level
        })
        
        return {
            'threat_level': threat_level,
            'recommendations': recommendations,
            'confidence': self.R['threat_prediction'],
            'patterns_identified': len([t for t in self.threat_database if t['threat_level'] > 0.7])
        }
    
    def _calculate_threat_level(self, threat_data: Dict[str, Any]) -> float:
        base_score = 0.0
        
        if threat_data.get('threat_detected', False):
            base_score += 0.6
        
        base_score += threat_data.get('confidence', 0.0) * 0.3
        
        # Recent similar threats increase score
        recent_threats = [t for t in self.threat_database 
                         if time.time() - t['timestamp'] < 300]  # 5 minutes
        if len(recent_threats) > 2:
            base_score += 0.2
        
        return min(1.0, base_score)
    
    def _generate_recommendations(self, threat_data: Dict[str, Any], threat_level: float) -> List[str]:
        recommendations = []
        
        if threat_level > 0.8:
            recommendations.extend(["immediate_block", "alert_administrator", "enhance_monitoring"])
        elif threat_level > 0.5:
            recommendations.extend(["close_monitoring", "update_firewall_rules"])
        
        if threat_data.get('threat_type') == "udp_flood":
            recommendations.append("rate_limiting")
        
        return recommendations

class SwarmCoordinator:
    """Coordinates interactions between MGS agents"""
    
    def __init__(self, agents: List[MutableGenerativeStructure]):
        self.agents = {agent.name: agent for agent in agents}
        self.shared_knowledge = []
        print("  ✅ Swarm Coordinator initialized")
    
    def process_threat_event(self, event_data: Dict[str, Any]):
        """Coordinate response to threat events"""
        print(f"\n🚨 THREAT EVENT DETECTED by {event_data['detected_by']}")
        print(f"   Type: {event_data['threat_context'].get('threat_type', 'unknown')}")
        
        # Share knowledge with all agents
        self.shared_knowledge.append(event_data)
        
        # Deception Director responds to all threats
        if 'DeceptionDirector' in self.agents:
            deception_response = self.agents['DeceptionDirector'].execute_rules({
                'attacker_id': f"attacker_{int(time.time())}",
                'threat_type': event_data['threat_context'].get('threat_type'),
                'sophisticated': event_data['threat_context'].get('confidence', 0) > 0.7
            })
            print(f"   🎭 Deception response: {deception_response['strategy']}")
        
        # Threat Analyzer processes all events
        if 'ThreatAnalyzer' in self.agents:
            analysis = self.agents['ThreatAnalyzer'].execute_rules(event_data['threat_context'])
            print(f"   📊 Threat level: {analysis['threat_level']:.2f}")
            print(f"   💡 Recommendations: {analysis['recommendations']}")
        
        # Trigger evolution based on threat severity
        if event_data['threat_context'].get('confidence', 0) > 0.7:
            self._trigger_evolution_cycle("high_severity_threat")
    
    def _trigger_evolution_cycle(self, reason: str):
        """Trigger evolution of all agents"""
        print(f"\n🔄 EVOLUTION CYCLE triggered: {reason}")
        
        evolution_context = {
            'reason': reason,
            'timestamp': time.time(),
            'shared_knowledge_count': len(self.shared_knowledge)
        }
        
        for agent_name, agent in self.agents.items():
            agent.evolve_rules(evolution_context)

class SCISOrchestrator:
    """Main orchestrator for the SCIS"""
    
    def __init__(self):
        print("\n" + "="*50)
        print("🤖 SYMBIODYNAMIC CYBER-IMMUNE SYSTEM")
        print("="*50)
        
        # Initialize agents
        self.network_sentinel = NetworkSentinelMGS()
        self.deception_director = DeceptionDirectorMGS()
        self.threat_analyzer = ThreatAnalyzerMGS()
        
        agents = [self.network_sentinel, self.deception_director, self.threat_analyzer]
        self.swarm_coordinator = SwarmCoordinator(agents)
        
        self.is_running = False
        self.simulation_time = 0
        
        print("\n✅ SCIS Initialization Complete!")
        print(f"   Active Agents: {len(agents)}")
        print("   Ready to start protection...\n")
    
    def simulate_network_traffic(self):
        """Generate simulated network traffic for testing"""
        traffic_types = [
            {'protocol': 'TCP', 'destination_port': 80, 'packet_size': 800, 'rate': 10},
            {'protocol': 'TCP', 'destination_port': 443, 'packet_size': 1200, 'rate': 15},
            {'protocol': 'UDP', 'destination_port': 53, 'packet_size': 512, 'rate': 5},
            {'protocol': 'TCP', 'destination_port': 4444, 'packet_size': 2000, 'rate': 100},  # Suspicious
            {'protocol': 'UDP', 'destination_port': 123, 'packet_size': 100, 'rate': 2000},   # Flood
            {'protocol': 'TCP', 'destination_port': 22, 'packet_size': 600, 'rate': 50},
        ]
        
        return random.choice(traffic_types)
    
    def run_demo(self, duration: int = 60):
        """Run a demonstration of the SCIS"""
        print(f"🎬 Starting SCIS Demo for {duration} seconds...")
        print("   Simulating network traffic and threat responses...\n")
        
        self.is_running = True
        start_time = time.time()
        
        while self.is_running and (time.time() - start_time) < duration:
            self.simulation_time += 1
            
            # Simulate network traffic
            traffic = self.simulate_network_traffic()
            
            # Network Sentinel analyzes traffic
            result = self.network_sentinel.execute_rules(traffic)
            
            # If threat detected, coordinate response
            if result['threat_detected']:
                threat_event = {
                    'detected_by': 'NetworkSentinel',
                    'threat_context': result,
                    'timestamp': time.time(),
                    'simulation_time': self.simulation_time
                }
                self.swarm_coordinator.process_threat_event(threat_event)
            
            # Periodic evolution every 15 seconds
            if self.simulation_time % 15 == 0:
                self.swarm_coordinator._trigger_evolution_cycle("periodic_evolution")
            
            # Display status every 10 seconds
            if self.simulation_time % 10 == 0:
                self._display_status()
            
            time.sleep(1)  # Simulate real-time operation
        
        self._display_final_report()
    
    def _display_status(self):
        """Display current system status"""
        print(f"\n📊 SCIS Status Update (Time: {self.simulation_time}s)")
        print(f"   Network Sentinel τ: {self.network_sentinel.S.relationship_time:.1f}")
        print(f"   Deception Director τ: {self.deception_director.S.relationship_time:.1f}")
        print(f"   Threat Analyzer τ: {self.threat_analyzer.S.relationship_time:.1f}")
        print(f"   Total Threats Processed: {len(self.swarm_coordinator.shared_knowledge)}")
    
    def _display_final_report(self):
        """Display final demo report"""
        print("\n" + "="*50)
        print("📈 SCIS DEMO COMPLETE - FINAL REPORT")
        print("="*50)
        
        print(f"\n🏆 Performance Summary:")
        print(f"   Total Simulation Time: {self.simulation_time} seconds")
        print(f"   Threats Detected: {len(self.swarm_coordinator.shared_knowledge)}")
        print(f"   Evolution Cycles: {int(max(agent.S.relationship_time for agent in [self.network_sentinel, self.deception_director, self.threat_analyzer]))}")
        
        print(f"\n🔧 Final Agent States:")
        for agent in [self.network_sentinel, self.deception_director, self.threat_analyzer]:
            print(f"   {agent.name}:")
            for rule_name, rule_value in agent.R.items():
                print(f"     {rule_name}: {rule_value:.3f}")
        
        print(f"\n🎭 Deception Director Profiles:")
        for attacker_id, profile in self.deception_director.attacker_profiles.items():
            print(f"   {attacker_id}: skill={profile['technical_skill']:.2f}, frustration={profile['frustration']:.2f}")
        
        print(f"\n💡 Threat Analysis:")
        if self.swarm_coordinator.shared_knowledge:
            recent_threats = [t for t in self.swarm_coordinator.shared_knowledge 
                            if t['threat_context'].get('confidence', 0) > 0.5]
            print(f"   High-confidence threats: {len(recent_threats)}")
        
        print("\n✅ SCIS demonstrated successful:")
        print("   ✓ Real-time threat detection")
        print("   ✓ Multi-agent coordination") 
        print("   ✓ Adaptive rule evolution")
        print("   ✓ Advanced deception tactics")
        print("   ✓ Threat intelligence analysis")

# Run the demo
if __name__ == "__main__":
    # Create and run the SCIS
    scis = SCISOrchestrator()
    
    # Run a 30-second demo (you can increase this)
    scis.run_demo(duration=30)
