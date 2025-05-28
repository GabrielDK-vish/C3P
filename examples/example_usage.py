import pandas as pd
from c3p import SmartAnalytic

def main():
    # Criar alguns DataFrames de exemplo
    df1 = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5],
        'Valor': [100, 200, 150, 300, 250],
        'Categoria': ['A', 'B', 'A', 'C', 'B']
    })
    
    df2 = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5],
        'Data': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15', '2023-03-01'],
        'Status': ['Ativo', 'Inativo', 'Ativo', 'Ativo', 'Inativo']
    })
    
    # Inicializar o analisador
    analyzer = SmartAnalytic()
    
    # Carregar os DataFrames
    analyzer.load_dataframes(df1, df2)
    
    # Carregar regras de um PDF (opcional)
    # analyzer.load_rules_pdf("regras_negocio.pdf")
    
    # Executar análise
    insights = analyzer.analyze()
    print("Insights gerados:")
    for i, insight in enumerate(insights, 1):
        print(f"{i}. {insight}")
    
    # Gerar relatório
    analyzer.generate_report("relatorio_analise.pdf")

if __name__ == "__main__":
    main()