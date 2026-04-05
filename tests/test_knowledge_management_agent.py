```json
{
    "tests/test_knowledge_management_agent.py": {
        "content": "
import logging
from typing import Dict, List
from AgentsService import KnowledgeManagementAgent
from Letta import MemoryManagement

class TestKnowledgeManagementAgent:
    def __init__(self):
        """
        Initialize the test class for KnowledgeManagementAgent.
        
        :return: None
        """
        self.knowledge_management_agent = KnowledgeManagementAgent()
        self.memory_management = MemoryManagement()
        self.logger = logging.getLogger(__name__)

    def test_non_stationary_drift_index(self, non_stationary_drift_index: List[float]) -> Dict[str, float]:
        """
        Test the non-stationary drift index calculation.
        
        :param non_stationary_drift_index: A list of non-stationary drift index values.
        :return: A dictionary containing the calculated non-stationary drift index.
        """
        try:
            self.logger.info('Testing non-stationary drift index calculation')
            result = self.knowledge_management_agent.calculate_non_stationary_drift_index(non_stationary_drift_index)
            return result
        except Exception as e:
            self.logger.error(f'Error calculating non-stationary drift index: {e}')
            return {}

    def test_stochastic_regime_switch(self, stochastic_regime_switch: List[float]) -> Dict[str, float]:
        """
        Test the stochastic regime switch calculation.
        
        :param stochastic_regime_switch: A list of stochastic regime switch values.
        :return: A dictionary containing the calculated stochastic regime switch.
        """
        try:
            self.logger.info('Testing stochastic regime switch calculation')
            result = self.knowledge_management_agent.calculate_stochastic_regime_switch(stochastic_regime_switch)
            return result
        except Exception as e:
            self.logger.error(f'Error calculating stochastic regime switch: {e}')
            return {}

    def test_memory_management(self, memory_management_data: Dict[str, str]) -> Dict[str, str]:
        """
        Test the memory management functionality.
        
        :param memory_management_data: A dictionary containing memory management data.
        :return: A dictionary containing the managed memory data.
        """
        try:
            self.logger.info('Testing memory management')
            result = self.memory_management.manage_memory(memory_management_data)
            return result
        except Exception as e:
            self.logger.error(f'Error managing memory: {e}')
            return {}

if __name__ == '__main__':
    test_knowledge_management_agent = TestKnowledgeManagementAgent()
    non_stationary_drift_index = [0.1, 0.2, 0.3]
    stochastic_regime_switch = [0.4, 0.5, 0.6]
    memory_management_data = {'key1': 'value1', 'key2': 'value2'}
    
    result1 = test_knowledge_management_agent.test_non_stationary_drift_index(non_stationary_drift_index)
    result2 = test_knowledge_management_agent.test_stochastic_regime_switch(stochastic_regime_switch)
    result3 = test_knowledge_management_agent.test_memory_management(memory_management_data)
    
    print('Non-stationary drift index result:', result1)
    print('Stochastic regime switch result:', result2)
    print('Memory management result:', result3)
",
        "commit_message": "feat: implement specialized test_knowledge_management_agent logic"
    }
}
```