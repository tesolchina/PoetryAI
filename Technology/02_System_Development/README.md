# System Development Phase

## Purpose
This folder contains all technical infrastructure, system architecture, and development components for the L2 Poetry Writing with LLMs research project.

## Contents

### Chat-Room Architecture
- **room configuration** - Chat room setup and configuration parameters
- **logging-system/**: System logging infrastructure for data collection

### Chatbot Framework
Complete AI chatbot implementation with comprehensive testing suite:

#### Core System
- `chatbot.py` - Main chatbot implementation
- `openrouter_client.py` - API integration layer
- `config/` - Configuration management system

#### Testing Suite
- `auto_test_poetry.py` - Automated poetry generation testing
- `comparison_test.py` - Comparative analysis tools
- `complete_analysis.py` - Comprehensive system analysis
- `test_models.py` - Model performance testing
- `test_poetry_request.py` - Poetry-specific request testing
- `three_types_test.py` - Three interaction types validation
- **chatbot testing/**: Complete testing documentation and results

#### Examples & Documentation
- `examples/` - Implementation examples and use cases
- `README.md` - Technical documentation
- **ui-design/**: User interface design specifications

## Technical Architecture
The system implements three distinct AI interaction types for L2 poetry writing:
1. **AI-guided writing**: Structured prompts and guidance
2. **AI-assisted revision**: Collaborative editing and feedback
3. **AI-collaborative creation**: Real-time co-creation

## Integration Points
- OpenRouter API for multiple LLM access
- Configurable personality and interaction modes
- Comprehensive logging for research data collection

## Next Phase
→ **03_Testing_Validation**: Systematic testing and validation procedures