#!/usr/bin/env python3
"""
Content Strategy & Hook Generator Tool
======================================
Extracted from 11 expert video transcripts

Usage:
    python main.py                          # Interactive mode
    python main.py --topic "email marketing" # Generate hooks
    python main.py --bulk "fitness"         # Generate 5 variations
    python main.py --analyze script.txt     # Analyze a script
    python main.py --frameworks             # List all frameworks
"""

import argparse
import sys
import os
from typing import Optional

from frameworks import ALL_FRAMEWORKS, list_all_frameworks, get_framework_by_name
from hook_generator import HookGenerator
from script_analyzer import ScriptAnalyzer, AnalysisResult


class Colors:
    """Terminal colors"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_banner():
    """Print the tool banner"""
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🎯 CONTENT STRATEGY & HOOK GENERATOR TOOL 🎯            ║
║                                                              ║
║     Based on 11 expert video transcripts                     ║
║     8 frameworks • 5 hook types • Auto-analysis              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}
"""
    print(banner)


def print_menu():
    """Print interactive menu"""
    menu = f"""
{Colors.BOLD}Choose an option:{Colors.ENDC}

  {Colors.GREEN}[1]{Colors.ENDC} Generate Hooks for a Topic
  {Colors.GREEN}[2]{Colors.ENDC} Bulk Generate (A/B Testing)
  {Colors.GREEN}[3]{Colors.ENDC} Analyze a Script/Hook
  {Colors.GREEN}[4]{Colors.ENDC} Browse Frameworks
  {Colors.GREEN}[5]{Colors.ENDC} Enhance Existing Hook
  {Colors.GREEN}[0]{Colors.ENDC} Exit
"""
    print(menu)


def interactive_mode():
    """Run interactive mode"""
    print_banner()
    
    generator = HookGenerator()
    analyzer = ScriptAnalyzer()
    
    while True:
        print_menu()
        choice = input(f"{Colors.BOLD}Enter choice (0-5): {Colors.ENDC}").strip()
        
        if choice == "0":
            print(f"\n{Colors.GREEN}Thanks for using the Content Strategy Tool! 👋{Colors.ENDC}\n")
            break
        
        elif choice == "1":
            topic = input(f"\nEnter topic (e.g., 'email marketing'): ").strip()
            if topic:
                print(f"\n{Colors.CYAN}Generating hooks for: {topic}{Colors.ENDC}\n")
                
                hooks = [
                    ("Contrarian", generator.generate_contrarian_hook(topic)),
                    ("Curiosity Gap", generator.generate_curiosity_hook(topic)),
                    ("Pain Agitation", generator.generate_pain_hook(topic)),
                    ("Social Proof", generator.generate_social_proof_hook(topic)),
                    ("How-To", generator.generate_how_to_hook(topic)),
                    ("3-Step Formula", generator.generate_three_step_hook(topic))
                ]
                
                for name, hook_data in hooks:
                    print(f"{Colors.GREEN}[{name}]{Colors.ENDC}")
                    print(f"  {hook_data['hook']}\n")
        
        elif choice == "2":
            topic = input(f"\nEnter topic for bulk generation: ").strip()
            if topic:
                count = input("Number of variations (default 5): ").strip()
                count = int(count) if count.isdigit() else 5
                
                print(f"\n{Colors.CYAN}Generating {count} hook variations for: {topic}{Colors.ENDC}\n")
                
                hooks = generator.generate_bulk_hooks(topic, count)
                for hook_data in hooks:
                    print(f"{Colors.GREEN}{hook_data['variation']} ({hook_data['framework']}){Colors.ENDC}")
                    print(f"  {hook_data['hook']}\n")
        
        elif choice == "3":
            print(f"\n{Colors.CYAN}Script Analysis{Colors.ENDC}")
            print("1. Enter text directly")
            print("2. Load from file")
            
            method = input("\nChoose method (1-2): ").strip()
            
            if method == "1":
                text = input("\nPaste your hook/script: ").strip()
                if text:
                    topic = input("Topic (optional): ").strip()
                    result = analyzer.analyze(text, topic)
                    analyzer.print_analysis(result)
            
            elif method == "2":
                filepath = input("\nEnter file path: ").strip()
                if os.path.exists(filepath):
                    with open(filepath, 'r') as f:
                        text = f.read()
                    topic = input("Topic (optional): ").strip()
                    result = analyzer.analyze(text, topic)
                    analyzer.print_analysis(result)
                else:
                    print(f"{Colors.RED}File not found: {filepath}{Colors.ENDC}")
        
        elif choice == "4":
            print(f"\n{Colors.CYAN}Available Frameworks:{Colors.ENDC}\n")
            for i, fw in enumerate(ALL_FRAMEWORKS, 1):
                print(f"{Colors.GREEN}[{i}]{Colors.ENDC} {fw.name}")
                print(f"    Source: {fw.source}")
                print(f"    {fw.description}\n")
            
            fw_choice = input("View details (1-8) or press Enter to continue: ").strip()
            if fw_choice.isdigit() and 1 <= int(fw_choice) <= 8:
                fw = ALL_FRAMEWORKS[int(fw_choice) - 1]
                print(f"\n{Colors.BOLD}{fw.name}{Colors.ENDC}")
                print(f"Source: {fw.source}")
                print(f"\n{fw.description}\n")
                print("Components:")
                for comp in fw.components:
                    print(f"  • {comp}")
                print("\nExamples:")
                for ex in fw.examples:
                    print(f"  {ex}")
                print()
        
        elif choice == "5":
            hook = input("\nEnter hook to enhance: ").strip()
            if hook:
                enhanced = generator.enhance_hook(hook)
                print(f"\n{Colors.GREEN}Original:{Colors.ENDC} {hook}")
                print(f"{Colors.GREEN}Enhanced:{Colors.ENDC} {enhanced}")
                
                # Analyze both
                print(f"\n{Colors.CYAN}Original Analysis:{Colors.ENDC}")
                orig_result = analyzer.analyze(hook)
                print(f"  Score: {orig_result.score}/100 - {orig_result.grade}")
                
                print(f"\n{Colors.CYAN}Enhanced Analysis:{Colors.ENDC}")
                enhanced_result = analyzer.analyze(enhanced)
                print(f"  Score: {enhanced_result.score}/100 - {enhanced_result.grade}")
                print()
        
        else:
            print(f"{Colors.RED}Invalid choice. Please try again.{Colors.ENDC}\n")


def cli_mode(args):
    """Run CLI mode with arguments"""
    generator = HookGenerator()
    analyzer = ScriptAnalyzer()
    
    if args.frameworks:
        print("\n📚 CONTENT STRATEGY FRAMEWORKS\n")
        print("=" * 60)
        for fw in ALL_FRAMEWORKS:
            print(f"\n🎯 {fw.name}")
            print(f"   Source: {fw.source}")
            print(f"   {fw.description}")
            print(f"\n   Key Components:")
            for comp in fw.components:
                print(f"      • {comp}")
        print("\n" + "=" * 60)
        return
    
    if args.topic:
        print_banner()
        print(f"\n🎯 Topic: {args.topic}\n")
        
        if args.bulk:
            count = args.bulk if isinstance(args.bulk, int) else 5
            print(f"📊 Generating {count} hook variations...\n")
            hooks = generator.generate_bulk_hooks(args.topic, count)
            
            for hook_data in hooks:
                print(f"{hook_data['variation']} ({hook_data['framework']})")
                print(f"   {hook_data['hook']}\n")
        else:
            print("📝 Generated Hooks:\n")
            
            hooks = [
                ("Contrarian", generator.generate_contrarian_hook(args.topic)),
                ("Curiosity Gap", generator.generate_curiosity_hook(args.topic)),
                ("Pain Agitation", generator.generate_pain_hook(args.topic)),
                ("Social Proof", generator.generate_social_proof_hook(args.topic)),
                ("How-To", generator.generate_how_to_hook(args.topic)),
                ("3-Step Formula", generator.generate_three_step_hook(args.topic))
            ]
            
            for name, hook_data in hooks:
                print(f"[{name}]")
                print(f"   {hook_data['hook']}\n")
        
        return
    
    if args.analyze:
        print_banner()
        
        if os.path.exists(args.analyze):
            with open(args.analyze, 'r') as f:
                text = f.read()
            print(f"\n📄 Analyzing: {args.analyze}\n")
        else:
            text = args.analyze
            print(f"\n📄 Analyzing provided text\n")
        
        result = analyzer.analyze(text, args.topic if args.topic else "")
        analyzer.print_analysis(result)
        return
    
    if args.enhance:
        print_banner()
        print(f"\n✨ Enhancing hook...\n")
        print(f"Original: {args.enhance}")
        enhanced = generator.enhance_hook(args.enhance)
        print(f"Enhanced: {enhanced}\n")
        
        print("📊 Analysis Comparison:")
        orig = analyzer.analyze(args.enhance)
        enh = analyzer.analyze(enhanced)
        print(f"   Original:  {orig.score}/100 ({orig.grade})")
        print(f"   Enhanced:  {enh.score}/100 ({enh.grade})")
        return
    
    # No arguments - show help
    print_banner()
    print("\nRun with --help for usage information")
    print("Or run without arguments for interactive mode\n")
    interactive_mode()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Content Strategy & Hook Generator Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                              # Interactive mode
  python main.py --topic "email marketing"    # Generate hooks
  python main.py --topic "fitness" --bulk 10  # Generate 10 variations
  python main.py --analyze "your hook text"   # Analyze a hook
  python main.py --analyze script.txt         # Analyze from file
  python main.py --frameworks                 # List all frameworks
  python main.py --enhance "your weak hook"   # Enhance a hook
        """
    )
    
    parser.add_argument(
        "--topic", "-t",
        type=str,
        help="Topic for hook generation (e.g., 'email marketing')"
    )
    
    parser.add_argument(
        "--bulk", "-b",
        nargs="?",
        const=5,
        type=int,
        metavar="N",
        help="Generate N hook variations for A/B testing (default: 5)"
    )
    
    parser.add_argument(
        "--analyze", "-a",
        type=str,
        metavar="TEXT/FILE",
        help="Analyze a hook or script (text or file path)"
    )
    
    parser.add_argument(
        "--frameworks", "-f",
        action="store_true",
        help="Display all available frameworks"
    )
    
    parser.add_argument(
        "--enhance", "-e",
        type=str,
        metavar="HOOK",
        help="Enhance an existing hook with power words"
    )
    
    args = parser.parse_args()
    
    # Check if any arguments provided
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        cli_mode(args)


if __name__ == "__main__":
    main()
