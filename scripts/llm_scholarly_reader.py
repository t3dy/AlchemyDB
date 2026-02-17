import json
from pathlib import Path

def aggregate_findings():
    findings_dir = Path("data")
    aggregated = {}
    
    # Load all findings
    files = ["substance_findings.json", "equipment_findings.json", "process_findings.json"]
    for filename in files:
        filepath = findings_dir / filename
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                category = filename.split("_")[0]
                for item in data:
                    term = item["term"]
                    if term not in aggregated:
                        aggregated[term] = {"category": category, "contexts": [], "metadata": item}
                    aggregated[term]["contexts"].append(item["context"])
    
    return aggregated

def generate_synthesis_prompts(aggregated):
    prompts = []
    for term, data in aggregated.items():
        prompt = f"### Term: {term} ({data['category']})\n"
        prompt += f"Contexts from corpus:\n"
        for i, ctx in enumerate(data["contexts"][:3]): # Limiting context for the summary
            prompt += f"--- Context {i+1} ---\n{ctx}\n"
        
        prompt += "\nTASK: Synthesize a 'Dual-History' dictionary entry following the AlchemyDB template.\n"
        prompt += "1. Core Definition\n2. Alchemical Profile (Theoretical/Symbolic)\n3. Modern Chemical Profile (Identified substance/reaction)\n4. Synthesis (Relational analysis)\n"
        prompts.append(prompt)
    
    output_file = Path("data/synthesis_prompts.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(prompts))
    
    print(f"Generated {len(prompts)} synthesis prompts in {output_file}")

if __name__ == "__main__":
    agg = aggregate_findings()
    generate_synthesis_prompts(agg)
