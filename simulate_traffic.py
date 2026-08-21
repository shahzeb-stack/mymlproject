import time
import random

def simulate_viral_traffic():
    print("--- [AIOps Cluster Monitor Active] Monitoring Virtual Pod Nodes ---")
    current_pods = 2  # Matches your minReplicas inside autoscaler.yaml
    total_requests = 0
    
    try:
        while True:
            total_requests += 1
            # Simulate a massive wave of incoming user text requests
            virtual_cpu_load = random.uniform(40, 98)
            print(f"Traffic Wave [Req #{total_requests}] -> Current Cluster CPU Load: {virtual_cpu_load:.1f}%")
            
            # AIOps Auto-scaling rule: target averageUtilization is 75%
            if virtual_cpu_load > 75.0 and current_pods < 10:
                current_pods += 1
                print(f"🚀 [AUTOSCALER ALERT] CPU crossed 75% threshold! Spawning new Pod. Scale out: {current_pods} Pods active.")
            elif virtual_cpu_load < 50.0 and current_pods > 2:
                current_pods -= 1
                print(f"📉 [AUTOSCALER NOTICE] Traffic cooling down. Terminating idle instance. Scale in: {current_pods} Pods active.")
                
            time.sleep(0.5)  # Speeds up the traffic simulation ticks
            
    except KeyboardInterrupt:
        print("\nTraffic simulator paused safely.")

if __name__ == "__main__":
    simulate_viral_traffic()

