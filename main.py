import sys
from sms_optimizer import SMSOOptimizer 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <drive1> <drive2> ...")
        exit(1)

    optimizer = SMSOOptimizer()
    plan = optimizer.optimize_storage(sys.argv[1:])

    for action in plan:
        print(f"Move '{action['file']}' to '{action['target_drive']}'")
