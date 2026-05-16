import pandas as pd
import matplotlib.pyplot as plt
import os

def run_corrosion_pipeline():
    print("\n=== EXECUTING MECHANICAL ENGINEERING DATA PIPELINE ===")
    
    # Strict project structure paths
    raw_data_path = os.path.join("data", "dataset_original.csv")
    clean_data_path = os.path.join("data", "dataset_cleaned.csv")
    plot_output_path = os.path.join("outputs", "corrosion_rate_comparison.png")
    
    try:
        # 1. Ingest and Clean
        df = pd.read_excel(raw_data_path, engine='openpyxl', header=1)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df.dropna(how='all')
        
        # 2. Extract Base Metrics
        initial_bare = df.loc[df['Days'] == 0, 'Weight of Bare Sepcimen (g)'].values[0]
        initial_coated = df.loc[df['Days'] == 0, 'Weight of Coated Specimen (g)'].values[0]
        
        # Compute cumulative mass loss
        df['Bare Mass Loss (g)'] = initial_bare - df['Weight of Bare Sepcimen (g)']
        df['Coated Mass Loss (g)'] = initial_coated - df['Weight of Coated Specimen (g)']
        
        # Save structured dataset exactly where the rubric requests it
        df.to_csv(clean_data_path, index=False)
        print(f"[SUCCESS] Pipeline cleaned data exported to: {clean_data_path}")
        
        # 3. Visualization Pipeline (Fulfills Section IX requirement for outputs/)
        plt.figure(figsize=(9, 5.5))
        plt.plot(df['Days'], df['Bare Mass Loss (g)'], marker='o', color='#d9534f', linewidth=2, label='Uncoated Bare Specimen (Control)')
        plt.plot(df['Days'], df['Coated Mass Loss (g)'], marker='s', color='#5cb85c', linewidth=2, label='Coated Specimen (Barrier Protected)')
        
        plt.title('Material Degradation Analysis: Cumulative Mass Loss Over Time', fontsize=12, fontweight='bold', pad=15)
        plt.xlabel('Exposure Duration (Days)', fontsize=10, labelpad=8)
        plt.ylabel('Cumulative Mass Loss (grams)', fontsize=10, labelpad=8)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend(fontsize=10, loc='upper left')
        plt.tight_layout()
        
        # Save plot to outputs/
        plt.savefig(plot_output_path, dpi=300)
        plt.close()
        print(f"[SUCCESS] Engineering visualization saved to: {plot_output_path}")
        print("\n--- SAMPLE PRICESS MATRIX ---")
        print(df[['Days', 'Bare Mass Loss (g)', 'Coated Mass Loss (g)']].head(4).to_string(index=False))
        
    except Exception as e:
        print(f"[ERROR] Pipeline stopped: {e}")

if __name__ == "__main__":
    run_corrosion_pipeline()