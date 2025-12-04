"""
Image Generation using Nanobanna API via OpenRouter
For generating visual assets for the PoetryAI research project
"""

import requests
import os
from typing import Optional
import json
from datetime import datetime
from pathlib import Path

# Load environment variables from .env file
def load_env():
    env_path = Path(__file__).parent.parent.parent / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

load_env()

class ImageGenerator:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the image generator with OpenRouter API
        
        Args:
            api_key: OpenRouter API key (if not provided, will look for OPENROUTER_API_KEY env var)
        """
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set OPENROUTER_API_KEY environment variable or pass api_key parameter")
        
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_image(self, prompt: str, model: str = "google/gemini-2.0-flash-exp:image-generation", 
                      save_path: Optional[str] = None) -> dict:
        """
        Generate an image using the specified model
        
        Args:
            prompt: Text description of the image to generate
            model: Model identifier (check OpenRouter docs for Nanobanna/Imagen models)
            save_path: Optional path to save the generated image
        
        Returns:
            Response dictionary containing image URL or data
        """
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            
            # Save response to file if path provided
            if save_path:
                self._save_response(result, save_path, prompt)
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"Error generating image: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            raise
    
    def _save_response(self, response: dict, save_path: str, prompt: str):
        """Save the API response and metadata"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON response
        json_path = f"{save_path}_{timestamp}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                "prompt": prompt,
                "timestamp": timestamp,
                "response": response
            }, f, indent=2)
        
        print(f"Response saved to: {json_path}")
        
        # If response contains image URL, print it
        if 'choices' in response and len(response['choices']) > 0:
            content = response['choices'][0].get('message', {}).get('content', '')
            print(f"Generated content: {content}")


def generate_research_diagrams():
    """Generate diagrams for the poetry research paper based on preliminary results"""
    
    generator = ImageGenerator()
    
    # Research-specific prompts based on the preliminary results essay
    prompts = {
        "fig1_interaction_distribution": """
        Create a professional academic bar chart comparing interaction type distribution across parameter conditions.
        Title: "Interaction Type Distribution by Parameter Configuration"
        Two groups side by side:
        - Low Temperature (0.3/0.4): Type A 60%, Type B 35%, Type C 5%
        - High Temperature (0.8/0.9): Type A 20%, Type B 45%, Type C 35%
        Use three distinct colors for each interaction type. Include clear labels and legend.
        Academic journal quality, clean design, suitable for publication.
        Highlight the 7x difference in Type C (5% vs 35%).
        """,
        
        "fig2_authorship_satisfaction": """
        Create a dual-axis chart showing authorship and satisfaction outcomes.
        Title: "Authorship Perception and Satisfaction by Parameter Configuration"
        X-axis: Low Temperature (0.3/0.4) vs High Temperature (0.8/0.9)
        Left Y-axis: Self-Authorship percentage (0-100%)
        Right Y-axis: Satisfaction rating (0-5)
        Data points:
        - Low temp: 10-20% authorship (bar), 2.0/5 satisfaction (line)
        - High temp: 62.5% authorship (bar), 4.75/5 satisfaction (line)
        Show 6x authorship difference and 90% satisfaction gap.
        Professional academic style with clear annotations.
        """,
        
        "fig3_three_types_framework": """
        Create a conceptual diagram illustrating the three interaction types framework.
        Title: "Three Interaction Types in AI-Assisted L2 Poetry Writing"
        Three connected boxes with arrows:
        1. Type A: Constraint Repair - "AI identifies issues, provides corrections" 
           (Lyster & Ranta, 1997 - diagnostic tool)
        2. Type B: Exemplar Giving - "AI provides model texts, line options for selection"
           (Hanauer, 2010 - scaffolded learning)
        3. Type C: Surprise Harvest - "AI generates unexpected possibilities, inspires new directions"
           (Coenen et al., 2022 - serendipitous discovery)
        Show how parameters influence which type dominates.
        Clean, modern academic design with theoretical foundations noted.
        """,
        
        "fig4_type_c_prediction": """
        Create a scatter plot or correlation visualization showing Type C predicting outcomes.
        Title: "Type C Presence Predicts Authorship and Satisfaction"
        Show relationship between Type C percentage and two outcomes:
        - 5% Type C → 10-20% authorship, 2.0/5 satisfaction (Low temp rooms A, B)
        - 35% Type C → 62.5% authorship, 4.75/5 satisfaction (High temp rooms C, D)
        Include trend lines or arrows showing positive correlation.
        Emphasize the mechanistic pathway: Type C enables active co-creation.
        Professional academic visualization suitable for research publication.
        """
    }
    
    output_dir = "Manuscript/graphies"
    os.makedirs(output_dir, exist_ok=True)
    
    for name, prompt in prompts.items():
        print(f"\nGenerating: {name}")
        print(f"Prompt: {prompt[:100]}...")
        
        try:
            result = generator.generate_image(
                prompt=prompt,
                save_path=f"{output_dir}/{name}"
            )
            print(f"✓ Successfully generated {name}")
        except Exception as e:
            print(f"✗ Failed to generate {name}: {e}")


def main():
    """Main function to test image generation"""
    
    # Check if API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("⚠️  OPENROUTER_API_KEY environment variable not set")
        print("Please set it with: $env:OPENROUTER_API_KEY='your-key-here'")
        return
    
    print("=== PoetryAI Image Generation ===\n")
    
    # Option 1: Generate research diagrams
    print("Generating research diagrams...")
    generate_research_diagrams()
    
    # Option 2: Custom generation
    # generator = ImageGenerator()
    # result = generator.generate_image(
    #     prompt="Your custom prompt here",
    #     save_path="output/custom_image"
    # )


if __name__ == "__main__":
    main()
