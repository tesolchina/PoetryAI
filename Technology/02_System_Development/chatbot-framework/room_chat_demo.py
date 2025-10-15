"""
PoetryAI Room Chat Demo
Demonstrates the room-based chat system for research
"""

import asyncio
import sys
from pathlib import Path

# Add the chatbot-framework directory to Python path
sys.path.append(str(Path(__file__).parent))

from room_chat import (
    PoetryRoomChat, 
    RoomType, 
    create_room_1, 
    create_room_2, 
    create_room_3, 
    create_room_4
)


async def interactive_demo():
    """Interactive demo of the room chat system"""
    print("🎭 PoetryAI Room Chat System Demo")
    print("=" * 50)
    
    # Room selection
    print("\nSelect a room:")
    print("1. Room 1: Structured + Aware")
    print("2. Room 2: Structured + Unaware") 
    print("3. Room 3: Exploratory + Aware")
    print("4. Room 4: Exploratory + Unaware")
    
    room_choice = input("\nEnter room number (1-4): ").strip()
    
    # Create room instance
    room_creators = {
        "1": create_room_1,
        "2": create_room_2, 
        "3": create_room_3,
        "4": create_room_4
    }
    
    if room_choice not in room_creators:
        print("Invalid choice. Using Room 2 (Structured + Unaware)")
        room = create_room_2()
    else:
        room = room_creators[room_choice]()
    
    print(f"\n📍 Connected to: {room.room_config.display_name}")
    print(f"   Parameters: Temperature={room.room_config.temperature}, Top-p={room.room_config.top_p}")
    
    # Start session
    participant_id = input("\nEnter participant ID (or press Enter for default): ").strip()
    if not participant_id:
        participant_id = "demo_participant"
    
    welcome_msg = room.start_session(participant_id)
    print(f"\n🤖 {welcome_msg}")
    
    # Chat loop
    print(f"\n💬 Chat started! Type 'quit' to end session.")
    print("=" * 50)
    
    while True:
        user_input = input(f"\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'end']:
            break
        
        if not user_input:
            continue
        
        try:
            # Get bot response
            bot_response = await room.send_message(user_input)
            print(f"🤖 Bot: {bot_response}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # End session
    notes = input("\n📝 Session notes (optional): ").strip()
    summary = room.end_session(notes)
    
    print(f"\n📊 Session Summary:")
    print("=" * 30)
    print(f"Room: {summary['room_type']}")
    print(f"Participant: {summary['participant_id']}")
    print(f"Total interactions: {summary['total_interactions']}")
    print(f"Duration: {summary['duration_minutes']} minutes")
    print(f"\nInteraction types:")
    for interaction_type, count in summary['interaction_type_counts'].items():
        print(f"  {interaction_type}: {count}")
    
    # Export option
    export_choice = input(f"\n💾 Export session data? (y/n): ").strip().lower()
    if export_choice in ['y', 'yes']:
        export_file = room.export_room_data()
        print(f"✅ Data exported to: {export_file}")


async def automated_demo():
    """Automated demo with predefined conversation"""
    print("🤖 Automated Demo: Room Comparison")
    print("=" * 50)
    
    # Test messages for comparison
    test_messages = [
        "I want to write a haiku about rain",
        "Help me count syllables in 'gentle rain falls down'", 
        "Can you show me an example of a good haiku?",
        "I'm stuck and need creative ideas for nature poetry"
    ]
    
    # Test both structured and exploratory rooms
    rooms_to_test = [
        ("Room 2: Structured + Unaware", create_room_2()),
        ("Room 4: Exploratory + Unaware", create_room_4())
    ]
    
    for room_name, room in rooms_to_test:
        print(f"\n🏠 Testing {room_name}")
        print(f"   Parameters: T={room.room_config.temperature}, Top-p={room.room_config.top_p}")
        print("-" * 40)
        
        # Start session
        welcome_msg = room.start_session("auto_test_participant")
        print(f"Welcome: {welcome_msg[:100]}...")
        
        # Send test messages
        for i, message in enumerate(test_messages, 1):
            print(f"\n{i}. User: {message}")
            try:
                response = await room.send_message(message)
                print(f"   Bot: {response}")
            except Exception as e:
                print(f"   Error: {e}")
        
        # End session and show summary
        summary = room.end_session("Automated test completed")
        print(f"\n📊 {room_name} Summary:")
        print(f"   Interactions: {summary['total_interactions']}")
        print(f"   Type A: {summary['interaction_type_counts']['type_a_diagnosis_repair']}")
        print(f"   Type B: {summary['interaction_type_counts']['type_b_exemplar_pivot']}")
        print(f"   Type C: {summary['interaction_type_counts']['type_c_surprise_harvest']}")


def main():
    """Main demo function"""
    print("PoetryAI Room Chat System")
    print("Choose demo mode:")
    print("1. Interactive chat")
    print("2. Automated comparison")
    
    choice = input("\nEnter choice (1-2): ").strip()
    
    if choice == "2":
        asyncio.run(automated_demo())
    else:
        asyncio.run(interactive_demo())


if __name__ == "__main__":
    main()