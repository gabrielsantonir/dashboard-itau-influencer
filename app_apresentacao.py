import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Configuração de Cores Itaú
ITAU_ORANGE = "#EC7000"
ITAU_BLUE = "#003399"
ITAU_YELLOW = "#FFCC00"
WHITE = "#FFFFFF"
GRAY = "#F0F2F6"

st.set_page_config(page_title="Estratégia Banco do Influencer", layout="wide", initial_sidebar_state="expanded")

# Customização Visual via CSS
st.markdown(f"""
    <style>
    /* Ajustes da barra lateral */
    [data-testid="stSidebar"] {{
        background-color: {ITAU_BLUE};
    }}
    [data-testid="stSidebar"] * {{
        color: {WHITE} !important;
    }}
    /* Títulos principais em laranja e azul */
    h1, h2, h3 {{ color: {ITAU_BLUE}; font-family: 'Arial', sans-serif; }}
    h1 {{ border-bottom: 3px solid {ITAU_ORANGE}; padding-bottom: 10px; font-size: 24px !important; }}
    
    /* Caixas de destaque e defesas */
    .defense-box {{ background-color: {GRAY}; padding: 20px; border-radius: 8px; border-left: 4px solid {ITAU_ORANGE}; margin-bottom: 20px; color: #333333; }}
    .defense-box h4 {{ color: {ITAU_ORANGE}; margin-top:0; }}
    
    hr {{ border-color: {ITAU_ORANGE}; opacity: 0.5; margin: 10px 0; }}
    
    /* Ajustes para caber na tela sem rolagem */
    [data-testid="block-container"] {{ padding-top: 1.5rem; padding-bottom: 0rem; }}
    .stMetric {{ padding: 10px 15px !important; }}
    
    /* Estilo para Tooltip */
    .tooltip {{
        position: relative;
        display: inline-block;
        border-bottom: 2px dotted {ITAU_ORANGE};
        cursor: pointer;
        color: {ITAU_ORANGE};
        font-weight: bold;
    }}
    .tooltip .tooltiptext {{
        visibility: hidden;
        width: 450px;
        background-color: #333333;
        color: #ffffff;
        text-align: left;
        border-radius: 8px;
        padding: 15px;
        position: absolute;
        z-index: 100;
        bottom: 125%;
        left: 50%;
        margin-left: -225px;
        opacity: 0;

        transition: opacity 0.3s;
        font-size: 12px;
        line-height: 1.4;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        border: 1px solid {ITAU_ORANGE};
    }}
    .tooltip:hover .tooltiptext {{
        visibility: visible;
        opacity: 1;
    }}
    </style>
    """, unsafe_allow_html=True)

# Navegação lateral
st.sidebar.image("logo_itau_oficial.png", width=80)
st.sidebar.markdown("### Itaú | Influencers")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navegação da Estratégia", [
    "0. Apresentação",
    "1. Resumo do Case",
    "2. Diagnóstico P&L", 
    "3. Direcionamento Estratégico", 
    "4. Proposta de Valor", 
    "5. Governança e Influência",
    "6. Plano de Ação",
    "7. KPIs e Trade-offs",
    "8. Influência Transversal Baseada em Dados", 
    "9. Visioning: Impacto",
    "10. Frame Mental",
    "11. Produtos e Serviços",
    "12. Agradecimento"
])


# --- PÁGINA 0: APRESENTAÇÃO ---
if page == "0. Apresentação":
    import base64
    def get_base64(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    logo_base64 = get_base64("logo_itau_oficial.png")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='text-align: center; background-color: {GRAY}; padding: 60px; border-radius: 15px; border-top: 8px solid {ITAU_ORANGE}; box-shadow: 0 4px 20px rgba(0,0,0,0.1);'>
            <img src='data:image/png;base64,{logo_base64}' width='100' style='margin-bottom: 30px;'>
            <h1 style='color: {ITAU_BLUE}; font-size: 42px; margin-bottom: 10px; border-bottom: none;'>Case de Seleção – Analista Sênior</h1>
            <h3 style='color: {ITAU_ORANGE}; font-weight: normal; margin-top: 0;'>Estratégia e Performance: Itaú o Banco do Influencer</h3>
            <div style='margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;'>
                <p style='font-size: 20px; color: #333; margin-bottom: 5px;'><b>Apresentado por:</b> Gabriel Augusto</p>
                <p style='font-size: 18px; color: #666;'>Abril, 2026</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align: center; color: #999;'>Navegue pelas páginas no menu lateral para visualizar o diagnóstico e o plano estratégico.</p>", unsafe_allow_html=True)


# --- PÁGINA 1: RESUMO DO CASE ---
elif page == "1. Resumo do Case":
    st.markdown("<h3 style='margin-bottom: 0px;'>📋 1. Resumo do Case: Influencers</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    col_metrics, col_chart = st.columns([1, 2])
    
    with col_metrics:
        st.markdown("#### O Cenário")
        st.metric("Mercado Endereçável", "16,9M")
        st.metric("Presença Itaú", "5,0M", delta="Base Analisada")
    
    with col_chart:
        df_base = pd.DataFrame({
            "Segmento": ["Monoliners", "Secundários", "Principais"],
            "Clientes (M)": [1.5, 2.0, 1.4]
        })
        fig_base = px.pie(df_base, values='Clientes (M)', names='Segmento', hole=.4,
                          color_discrete_sequence=[ITAU_ORANGE, ITAU_BLUE, "#333333"])
        fig_base.update_traces(textfont_color='white', textinfo='percent+label', textposition='inside')
        fig_base.update_layout(height=280, margin=dict(t=0, b=0, l=0, r=0), showlegend=True)
        st.plotly_chart(fig_base, use_container_width=True)
    colA, colB, colC = st.columns(3)
    with colA:
        st.markdown(f"<div class='defense-box' style='min-height: 140px; padding: 10px; border-top: 4px solid {ITAU_ORANGE}; border-left: none;'><b>Monoliners (1,5M)</b><br><p style='font-size: 12px; margin-top: 5px;'>Apenas Cartão. Reconhecimento de marca sem vínculo transacional em conta.</p></div>", unsafe_allow_html=True)
    with colB:
        st.markdown(f"<div class='defense-box' style='min-height: 140px; padding: 10px; border-top: 4px solid {ITAU_BLUE}; border-left: none;'><b>Secundários (2,0M)</b><br><p style='font-size: 12px; margin-top: 5px;'>Conta aberta, mas sem utilização como banco principal de recebimento.</p></div>", unsafe_allow_html=True)
    with colC:
        st.markdown(f"<div class='defense-box' style='min-height: 140px; padding: 10px; border-top: 4px solid #333333; border-left: none;'><b>Principais (1,4M)</b><br><p style='font-size: 12px; margin-top: 5px;'>Conta corrente com vínculo de recebimento consolidado (domicílio bancário).</p></div>", unsafe_allow_html=True)



# --- PÁGINA 2: DIAGNÓSTICO P&L ---
elif page == "2. Diagnóstico P&L":

    st.markdown("""<style>
        table { font-size: 12px; margin-bottom: 0px !important; }
        th, td { padding: 4px 8px !important; line-height: 1.2 !important; }
        div[data-testid="metric-container"] { padding-top: 0px !important; padding-bottom: 10px !important; }
    </style>""", unsafe_allow_html=True)
    
    st.markdown("<h3 style='margin-bottom: 0px; padding-bottom: 5px; margin-top: 0px;'>📊 2. Diagnóstico P&L: Onde estamos hoje?</h3>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 0px 0px 10px 0px;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 13px; margin-bottom: 15px;'>Análise da base atual e identificação de oportunidades no mercado da 'economia de influência'.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Profit Share Atual", "35%", "-65% de fuga (Share of Wallet)")
    col2.metric("Eficiência Operacional", "58%", "Necessita digitalização")
    col3.metric("Mix Crédito/Cartão", "70%", "Alta dependência de spread")

    colA, colB = st.columns(2)
    with colA:
        # Gráfico de Mix de Receita
        df_mix = pd.DataFrame({
            "Produto": ["Crédito", "Cartão", "Seguros", "Investimentos"],
            "Percentual": [40, 30, 20, 10]
        })
        fig = px.pie(df_mix, values='Percentual', names='Produto', 
                     title="Mix de Receita Atual", hole=0.4,
                     color_discrete_sequence=[ITAU_BLUE, ITAU_ORANGE, ITAU_YELLOW, "#4A4A4A"])
        fig.update_traces(textposition='inside', textinfo='percent+label', textfont_color='white')
        fig.update_layout(height=260, margin=dict(t=30, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
        
    with colB:
        st.markdown("<h4 style='margin-bottom: 8px; margin-top: 0px; padding-bottom: 0;'>Contexto de Mercado</h4>", unsafe_allow_html=True)
        
        df_quadro = pd.DataFrame({
            "Métrica": ["Profit Share", "Eficiência", "Mix de Receita"],
            "Valor": ["35%", "58%", "70%"],
            "Diagnóstico do Analista": [
                "<b>Alavanca:</b> Itaú captura apenas 1/3 do valor (fuga de 65%).",
                "<b>Custo:</b> R$ 2,499 Bi Custo Operacional. Exige revisão.",
                "<b>Risco:</b> Sub-aproveitamento de Investimentos (apenas 10%)."
            ]
        })
        
        # Gerador nativo de tabela HTML Ultra-Compacta
        html_table = "<table style='width: 100%; border-collapse: collapse; margin-bottom: 12px; font-size: 12px;'>"
        html_table += "<tr style='border-bottom: 1px solid #444;'><th style='text-align:left;'>Métrica</th><th style='text-align:left;'>Valor</th><th style='text-align:left;'>Diagnóstico</th></tr>"
        for _, row in df_quadro.iterrows():
            html_table += f"<tr style='border-bottom: 1px solid #333;'><td><b>{row['Métrica']}</b></td><td>{row['Valor']}</td><td>{row['Diagnóstico do Analista']}</td></tr>"
        html_table += "</table>"
        
        st.markdown(html_table, unsafe_allow_html=True)

        st.markdown("<p style='font-size: 13px; margin-bottom: 2px; margin-top: 0px;'>• <b>Maiores Fontes:</b> Crédito (40%) e Cartões (30%) sustentam o P&L atual.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 13px; margin-bottom: 0px;'>• <b>Ameaça:</b> A baixa penetração em investimentos revela que não somos o banco principal.</p>", unsafe_allow_html=True)


# --- PÁGINA 3: DIRECIONAMENTO ESTRATÉGICO ---
elif page == "3. Direcionamento Estratégico":
    st.markdown("<h3 style='margin-bottom: 0px; padding-bottom: 5px; margin-top: 0px;'>🎯 3. Direcionamento Estratégico: 2026-2028</h3>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 0px 0px 10px 0px;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 13px; margin-bottom: 15px;'>Frentes prioritárias para captura de valor e adensamento da base.</p>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='defense-box' style='min-height: 260px;'><h4>Conversão de Monoliners</h4><p><b>(Ataque à Base):</b> Temos 1,5M de clientes que possuem apenas cartão. O foco é a conversão para conta corrente.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='defense-box' style='min-height: 260px;'><h4>Ativação de Principalidade</h4><p><b>(A Nossa \"Mina de Ouro\"):</b> Foco em converter os 2M de correntistas secundários em clientes com vínculo de recebimento.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='defense-box' style='min-height: 260px;'><h4>Expansão de Serviços</h4><p><b>(Cross-sell):</b> Elevar a receita de investimentos e seguros para 40% através de produtos de previdência para \"carreiras de ciclo curto\".</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='defense-box' style='min-height: 260px;'><h4>Eficiência de Atendimento</h4><p>Migrar o custo operacional de R$ 2,499 Bi para modelos de atendimento digital escalável, focando o esforço humano apenas em atendimento especializado para influenciadores.</p></div>", unsafe_allow_html=True)


# --- PÁGINA 4: PROPOSTA DE VALOR ---
elif page == "4. Proposta de Valor":

    st.markdown("<h3 style='margin-bottom: 0px; padding-bottom: 5px; margin-top: 0px;'>💎 4. Proposta de Valor</h3>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 0px 0px 10px 0px;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 13px; margin-bottom: 15px;'>Soluções especializadas para cada etapa do ciclo de vida do criador de conteúdo.</p>", unsafe_allow_html=True)
    
    tab_baixa, tab_media, tab_alta, tab_jornada = st.tabs(["Baixa Renda", "Média Renda", "Alta Renda", "Trajetória para Principalidade"])
    
    with tab_baixa:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""<div class='defense-box' style='min-height: 250px;'>
                <h4>Foco: Educação e Microcrédito</h4>
                <p><b>Objetivo:</b> Ser o parceiro de crescimento. Ajudamos o criador a profissionalizar sua produção desde o início.</p>
                <p><b>Nossa Proposta:</b> Através de educação financeira e microcrédito orientado, fornecemos as ferramentas para a evolução da carreira.</p>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div class='defense-box' style='min-height: 250px; border-left-color: {ITAU_BLUE};'>
                <h4>Benefício: Isenção por "Publis"</h4>
                <p><b>Alavanca de Principalidade:</b> Isenção de tarifas mediante recebimento de contratos na conta Itaú.</p>
                <p><b>Diferencial:</b> O nano-influenciador é sensível a taxas. Uma conta robusta sem custo fixo é o maior atrativo para garantir o domicílio bancário.</p>
            </div>""", unsafe_allow_html=True)
        
        st.info("**Visibilidade de Fluxo de Caixa:** O recebimento da 'publi' no Itaú permite ofertar crédito com menor risco e taxas mais competitivas, já que o fluxo nasce dentro de casa.")
        st.info("**Equilíbrio de Valor:** Esta ação abre mão da tarifa de conta para ganhar na principalidade e no relacionamento de longo prazo.")

    with tab_media:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""<div class='defense-box' style='min-height: 280px;'>
                <h4>Foco: Eficiência Tributária</h4>
                <p><b>A Solução (PJ):</b> O banco atua como consultor para abertura de empresa, reduzindo a carga tributária de 27,5% (PF) para a partir de 6% (Simples Nacional).</p>
                <p><b>O Valor:</b> Ajudar o cliente a 'sobrar mais dinheiro' gera satisfação ao cliente e principalidade para o banco.</p>
                <p><b>Jornada Única:</b> Visualização de saldos PF e PJ no mesmo app, facilitando a gestão do dia a dia.</p>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div class='defense-box' style='min-height: 280px; border-left-color: {ITAU_BLUE};'>
                <h4>Proposta: Profissionalização</h4>
                <p><b>Integração PF+PJ:</b> Ao integrar as jornadas, garantimos a principalidade do recebimento de grandes contratos de agências.</p>
                <p><b>Limite Unificado:</b> O faturamento da PJ é considerado para limites de crédito maiores no CPF, resolvendo uma dor histórica do setor.</p>
                <p><b>Mitigação de Risco:</b> A visão do faturamento PJ permite monitorar a saúde financeira real e prevenir inadimplência.</p>
            </div>""", unsafe_allow_html=True)
        
        st.info("**Fluxo de Recebimento:** Grandes agências de publicidade exigem nota fiscal e pagamento em conta PJ. O Itaú facilita o recebimento desses grandes contratos.")
        st.info("**Captura de Profit Share:** Atualmente em 35%. Ao trazer a conta PJ, 'fechamos o ecossistema', capturando lucro em todas as pontas (investimentos, cartões, faturamento).")

    with tab_alta:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""<div class='defense-box' style='border-left-color: {ITAU_ORANGE};'>
            <h4>Foco: Preservação de Patrimônio</h4>
            <p><b>Estratégia Ecossistema:</b> Identificamos que as celebridades usam o Itaú para transacionar, mas levavam a liquidez para competidores. O foco agora é reter esse patrimônio.</p>
        </div>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""<div class='defense-box' style='min-height: 220px; border-left-color: {ITAU_BLUE};'>
                <h4>Exclusividade: Influencer Desk</h4>
                <p>Implementação de um atendimento dedicado via <b>Itaú Private</b> para acesso a private equity, crédito estruturado e assessoria personalizada.</p>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div class='defense-box' style='min-height: 220px;'>
                <h4>Blindagem e Sucessão</h4>
                <p>Foco em <b>Planejamento Sucessório</b> e Estruturas Offshore para perenizar o patrimônio, considerando que são carreiras de ciclo curto e alta volatilidade.</p>
                <p><b>Seguro de Imagem:</b> Proteção específica contra riscos reputacionais.</p>
            </div>""", unsafe_allow_html=True)
        
        st.info("**Impacto no P&L:** Esta frente é a maior oportunidade de elevar o Profit Share para patamares de excelência. Ao capturar a custódia dos investimentos, aumentamos o LTV e transformamos o banco no pilar de segurança financeira do cliente.")

    with tab_jornada:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 🚀 Jornada do Influencer: O Caminho da Principalidade")
        
        st.markdown(f"""
        <div class='defense-box' style='border-top: 4px solid #003399; border-left: none;'>
            <h4 style='color: #003399;'>Fase 1: O Despertar (Baixa Renda / Nano-Influencer)</h4>
            <p style='font-size: 13px;'><i>O objetivo é a Conquista e Educação. O Itaú como o parceiro que acredita no potencial do criador.</i></p>
            <div style='display: flex; gap: 20px; margin-top: 10px;'>
                <div style='flex: 1;'>
                    <b>Gatilho:</b> Recebimento das primeiras "publis".<br>
                    <b>Ação:</b> Oferecer Conta Digital com Atrito Zero.
                </div>
                <div style='flex: 2;'>
                    <b>Proposta de Valor:</b>
                    <ul style='font-size: 13px;'>
                        <li>Isenção por Principalidade: Tarifa zero para domicílio bancário.</li>
                        <li>Educação Financeira: Conteúdo para profissionalização.</li>
                        <li>Microcrédito: Limites para equipamentos.</li>
                    </ul>
                </div>
            </div>
            <p style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; font-size: 12px; margin-top: 10px;'>
                <b>Ganho para o P&L:</b> Captura de dados. O fluxo em casa reduz risco de crédito e cria o hábito da principalidade.
            </p>
        </div>
        
        <div class='defense-box' style='border-top: 4px solid {ITAU_ORANGE}; border-left: none; margin-top: 20px;'>
            <h4 style='color: {ITAU_ORANGE};'>Fase 2: A Profissionalização (Média Renda / Micro e Mid)</h4>
            <p style='font-size: 13px;'><i>O objetivo é a Eficiência e Organização. O Itaú como Consultor de Transição PF → PJ.</i></p>
            <div style='display: flex; gap: 20px; margin-top: 10px;'>
                <div style='flex: 1;'>
                    <b>Gatilho:</b> Carga de 27,5% de IR na PF e exigência de Nota Fiscal.<br>
                    <b>Ação:</b> Consultoria para abertura de PJ (Simples Nacional).
                </div>
                <div style='flex: 2;'>
                    <b>Proposta de Valor:</b>
                    <ul style='font-size: 13px;'>
                        <li>Eficiência Tributária: Redução de impostos para ~6%.</li>
                        <li>Ecossistema Integrado: Visualização única PF+PJ no App.</li>
                        <li>Limite Unificado: Faturamento PJ garante limites no CPF.</li>
                    </ul>
                </div>
            </div>
            <p style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; font-size: 12px; margin-top: 10px;'>
                <b>Ganho para o P&L:</b> Aumento do Share of Wallet. "Fechamos o ecossistema" capturando lucro em todas as pontas.
            </p>
        </div>
        
        <div class='defense-box' style='border-top: 4px solid #333333; border-left: none; margin-top: 20px;'>
            <h4 style='color: #333333;'>Fase 3: A Consolidação e Legado (Alta Renda / Celebridades)</h4>
            <p style='font-size: 13px;'><i>O objetivo é a Preservação e Blindagem. Ativação do 'Influencer Desk' (Itaú Private).</i></p>
            <div style='display: flex; gap: 20px; margin-top: 10px;'>
                <div style='flex: 1;'>
                    <b>Gatilho:</b> Alta liquidez e necessidade de planejar pós-carreira.<br>
                    <b>Ação:</b> Acesso a Private Equity e Crédito Estruturado.
                </div>
                <div style='flex: 2;'>
                    <b>Proposta de Valor:</b>
                    <ul style='font-size: 13px;'>
                        <li>Gestão de Fortuna: Fundos exclusivos e blindagem patrimonial.</li>
                        <li>Seguros de Imagem: Proteção reputacional específica.</li>
                        <li>Sucessão/Offshore: Estruturas para perenizar o patrimônio.</li>
                    </ul>
                </div>
            </div>
            <p style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; font-size: 12px; margin-top: 10px;'>
                <b>Ganho para o P&L:</b> Custódia dos Investimentos (gap de 10%). Aumento drástico do LTV e segurança financeira total.
            </p>
        </div>
        """, unsafe_allow_html=True)


# --- PÁGINA 5: GOVERNANÇA E INFLUÊNCIA ---
elif page == "5. Governança e Influência":
    st.markdown("<h3 style='margin-bottom: 0px; padding-bottom: 5px; margin-top: 0px;'>🏗️ 5. Governança e Influência Transversal</h3>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 0px 0px 10px 0px;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 13px; margin-bottom: 15px;'>Atuação em Rede e Adensamento da Base.</p>", unsafe_allow_html=True)
    
    st.markdown("### Por que Priorizar o Adensamento?")
    st.info("Já possuímos uma base instalada de **5M de clientes** (1,5M monoliners, 2M secundários e 1,5M principais). O dado mais crítico do P&L é o nosso Profit Share de 35%, o que indica que 65% do valor gerado por esses clientes não está sendo fidelizado no Itaú, gerando espaço no mercado para os concorrentes.")
    
    colA, colB, colC = st.columns(3)
    with colA:
        st.markdown("<div class='defense-box' style='min-height: 240px;'><h4>Oportunidade Imediata</h4><p><b>1,5M de Monoliners:</b> Público com conhecimento da marca, porém com relacionamento restrito ao cartão. Representam nossa maior oportunidade de conversão imediata.</p></div>", unsafe_allow_html=True)
    with colB:
        st.markdown("<div class='defense-box' style='min-height: 240px; border-left-color: #003399;'><h4>Gap de Principalidade</h4><p><b>2M de Correntistas Secundários:</b> O maior gap da vertical. Clientes que já superaram a barreira da aquisição, mas cujo fluxo ainda reside na concorrência.</p></div>", unsafe_allow_html=True)
    with colC:
        st.markdown("<div class='defense-box' style='min-height: 240px;'><h4>Base de Principalidade</h4><p><b>1,5 Mi Principais:</b> Para a base de clientes com vínculo de recebimento, priorizaremos a identificação de perfis com potencial de investimento e expansão de serviços via cross-sell. O objetivo é mapear contas propensas a novas aquisições, fortalecendo o relacionamento e aumentando a rentabilidade operacional.</p></div>", unsafe_allow_html=True)


        
    st.write("")
    
    df_caminhos = pd.DataFrame({
        "Caminho": ["<b>Conquista<br>(Novos)</b>", "<b>Adensamento<br>(Base)</b>"],
        "Impacto Financeiro": [
            "Alto CAC (Custo de Aquisição). Gera volume, mas pode atrair clientes de baixa rentabilidade inicial.",
            "Redução do CAC marginal. Aumento do LTV (Life Time Value) e elevação do Profit Share."
        ],
        "Impacto Estratégico": [
            "Aumento de market share, mas risco de diluição da margem se não houver retenção rápida.",
            "Consolidação da Principalidade. O Itaú deixa de ser um cartão e vira o ecossistema financeiro do cliente."
        ]
    })
    
    # Construção da tabela em HTML sem indentação para evitar que o Markdown renderize como <pre> code block
    html_table = f"""<div style="display: flex; justify-content: center; margin-top: 10px;">
<table style="width: 90%; border-collapse: collapse; text-align: center; font-size: 14px; border: 1px solid #ddd;">
<tr style="background-color: {ITAU_BLUE}; color: white;">
<th style="padding: 10px; border: 1px solid #ddd; width: 20%;">Caminho</th>
<th style="padding: 10px; border: 1px solid #ddd; width: 40%;">Impacto Financeiro</th>
<th style="padding: 10px; border: 1px solid #ddd; width: 40%;">Impacto Estratégico</th>
</tr>"""
    for _, row in df_caminhos.iterrows():
        html_table += f"""
<tr style="background-color: {WHITE}; color: black;">
<td style="padding: 10px; border: 1px solid #ddd;">{row['Caminho']}</td>
<td style="padding: 10px; border: 1px solid #ddd; text-align: left;">{row['Impacto Financeiro']}</td>
<td style="padding: 10px; border: 1px solid #ddd; text-align: left;">{row['Impacto Estratégico']}</td>
</tr>"""
    html_table += "</table></div>"
    
    st.markdown(html_table, unsafe_allow_html=True)


# --- PÁGINA 6: PLANO DE AÇÃO ---
elif page == "6. Plano de Ação":
    st.title("🚀 6. Plano de Ação")
    st.markdown("---")

    
    tab1, tab2 = st.tabs(["Vetor de Principalidade e Adensamento", "Plano Estratégico Vertical Influencer"])
    
    with tab1:
        st.markdown("##### Plano de Ação: Vetor de Principalidade e Adensamento")

        st.write("O objetivo é elevar a receita de R$ 4,3 bilhões focando na diversificação do mix (atualmente 70% concentrado em crédito e cartões).")
        st.write("")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""<div class='defense-box' style='min-height: 400px;'>
                <h4>Ação A: Conversão de Monoliners (Foco: 1,5M de Cartonistas)</h4>
                <ul>
                    <li><b>Ação:</b> Oferta de <span class="tooltip">"Upgrade Automático"
                        <span class="tooltiptext">
                            <b>1. A Jornada "One-Click" (Atrito Zero)</b><br>
                            Como o banco já tem os dados cadastrais, foto (biometria) e histórico de crédito do Monoliner, ele não precisa passar pelo processo padrão de abertura de conta.<br><br>
                            <b>O Gatilho:</b> No app aparece um banner: "Sua conta digital está pronta. Ative com um clique e tenha 12 meses de isenção".<br><br>
                            <b>A Execução:</b> Ativação instantânea utilizando dados já existentes.<br><br>
                            <b>2. O "Hook" (Isca) da Isenção de Tarifa</b><br>
                            Oferecemos 12 meses de isenção total, renovada automaticamente se cadastrar o Itaú como domicílio bancário para suas "publis". Aqui você troca a receita de tarifa (baixa margem) pelo fluxo de caixa (alta margem).
                        </span>
                    </span> para conta corrente com isenção de tarifa por 12 meses para quem trouxer o domicílio bancário.</li><br>
                    <li><b>Impacto:</b> Reduz a dependência de Crédito Pessoal (40%) ao atrair depósitos à vista que barateiam o custo de captação do banco.</li>
                </ul>
            </div>""", unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""<div class='defense-box' style='min-height: 400px; border-left-color: {ITAU_BLUE};'>
                <h4>Ação B: Ativação de Principalidade (Foco: 2M de Correntistas Secundários)</h4>
                <ul>
                    <li><b>Ação:</b> Lançamento da "Jornada de Domicílio Premiado". Oferecer integração gratuita de conta PJ (Itaú Emps) com isenção de tarifas e linhas de crédito exclusivas para equipamentos (taxas diferenciadas) para quem centralizar o recebimento de contratos no Itaú.</li><br>
                    <li><b>Impacto:</b> Estanca a fuga de lucro para a concorrência, transformando contas inativas em contas transacionais principais e aumentando o Índice de Principalidade.</li>
                </ul>
            </div>""", unsafe_allow_html=True)

        with col3:
            st.markdown(f"""<div class='defense-box' style='min-height: 400px;'>
                <h4>Ação C: Alavancagem de Investimentos e Seguros (Ataque aos 30% do mix)</h4>
                <ul>
                    <li><b>Ação:</b> Criar "Gatilhos de Investimento" no app. Ao receber um faturamento acima de um valor X, o sistema sugere automaticamente a aplicação em fundos de liquidez ou previdência, além de ofertar seguros de imagem.</li><br>
                    <li><b>Impacto:</b> Eleva a participação de Investimentos (hoje 10%) e Seguros (20%) na receita total, equilibrando o risco do P&L.</li>
                </ul>
            </div>""", unsafe_allow_html=True)


            
    with tab2:
        st.markdown("##### Plano Estratégico Vertical Influencer")
        st.write("")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""<div class='defense-box' style='text-align: center; border-left: none; border-top: 4px solid #003399;'>
                <h1 style='border:none; margin-bottom:0;'>📊</h1>
                <h4 style='color:#003399; margin-top:5px;'>Diagnóstico Analítico</h4>
                <p><span class="tooltip">(O Cenário Atual)<span class="tooltiptext">Operamos em um mercado potencial de 16,9 milhões de clientes, capturando apenas 35% do Profit Share. O P&L revela alta dependência de spread de crédito (70% da receita) e sub-penetração crítica em Investimentos (10%).</span></span></p>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""<div class='defense-box' style='text-align: center; border-left: none; border-top: 4px solid #EC7000;'>
                <h1 style='border:none; margin-bottom:0;'>🎯</h1>
                <h4 style='color:#EC7000; margin-top:5px;'>Direcionamento Estratégico</h4>
                <p><span class="tooltip">(A Escolha)<span class="tooltiptext"><b>Conversão de 1,5M de Monoliners:</b> Migração do público de cartão para o ecossistema de conta corrente.<br><br><b>Ativação de 2M de Correntistas Secundários:</b> Transformar contas inativas ou secundárias em contas principais através do vínculo de recebimento (domicílio bancário), estancando a fuga de valor para a concorrência.</span></span></p>
            </div>""", unsafe_allow_html=True)
        with c3:
            st.markdown(f"""<div class='defense-box' style='text-align: center; border-left: none; border-top: 4px solid #333333;'>
                <h1 style='border:none; margin-bottom:0;'>⚙️</h1>
                <h4 style='color:#333333; margin-top:5px;'>Pilares de Atuação</h4>
                <p><span class="tooltip">(As Alavancas)<span class="tooltiptext"><b>Conversão e Ativação de Principalidade (Atrito Zero):</b> Foco na migração dos 1,5M de Monoliners e na ativação dos 2M de correntistas secundários. A alavanca central é o "Domicílio Bancário Premiado", trocando tarifas de conta pelo fluxo de caixa das "publis", garantindo que o Itaú se torne o ecossistema financeiro principal do influenciador.<br><br><b>Hiper-personalização da Proposta de Valor:</b> Segmentação consultiva baseada no ciclo de vida da carreira. Entregar desde ferramentas de profissionalização e microcrédito (Nano) até soluções complexas de eficiência tributária e planejamento sucessório (Média e Alta Renda).</span></span></p>
            </div>""", unsafe_allow_html=True)


        st.write("")
        st.success("**Visão de Impacto - O Resultado Esperado**  \nEm regime de um ano, as iniciativas visam um crescimento de receita para R$ 4,9 bilhões (incremento de 14%) e a expansão do Profit Share para 45%. Isso será sustentado por uma governança transversal forte, integrando as áreas de Produto, CRM e Operações para garantir a melhor experiência ao cliente.")


# --- PÁGINA 7: KPIs E TRADE-OFFS ---
elif page == "7. KPIs e Trade-offs":
    st.title("⚖️ 7. KPIs e Trade-offs Associados")
    st.markdown("---")

    st.markdown("Indicadores de Sucesso e Monitoramento.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Indicadores de Sucesso (KPIs)")
        st.write("1. **Profit Share:** Meta de sair de 35% para 45% em 3 anos.")
        st.write("2. **Índice de Principalidade:** % de clientes com vínculo de recebimento sobre o total de correntistas (Alvo: Migrar os 2M de secundários para o status de principal).")
        st.write("3. **Cross-sell Ratio:** Número médio de produtos por cliente (foco em elevar Seguros e Investimentos).")
        st.write("4. **Índice de Conversão Monoliner:** % de migração dos 1,5M de clientes de cartão para a conta corrente.")
        st.write("5. **Share of Wallet Diversificado:** Penetração de produtos de Investimento e Seguros na base de 5M.")
        st.write("6. **LTV/CAC:** Relação entre o valor que o cliente gera ao longo do tempo versus o custo para mantê-lo ou adquiri-lo.")
        st.write("7. **NPS (Net Promoter Score):** Meta de manter no Nível de Excelência (>75) (Métrica de Sustentabilidade do Relacionamento).")

        
    with col2:
        st.markdown("### Trade-offs Estratégicos")
        st.warning("• **Velocidade vs. Rentabilidade:** Optamos por um crescimento de base nominal mais cadenciado em troca de uma alavancagem imediata de rentabilidade. Priorizar o adensamento dos 2M de correntistas secundários e 1,5M de monoliners garante um LAIR (lucro) superior e mais rápido, visto que operamos com custo marginal de aquisição (CAC) zero para clientes que já estão na nossa base. A \"velocidade\" aqui é medida pela conversão em principalidade, e não apenas pelo volume de novas contas.")
        st.warning("• **Investimento em Tecnologia vs. Marketing:** Priorizamos o orçamento para o desenvolvimento de jornadas de produto e conversão (Ex: Integração PF+PJ, Dashboards de Eficiência Tributária e Gatilhos de Investimento). Entendemos que para o público Influencer, a funcionalidade do ecossistema e a experiência do app (UX) são ferramentas de retenção e adensamento muito mais baratas e eficazes do que campanhas de marketing de massa. Investimos na \"casa\" para garantir que o cliente secundário escolha o Itaú como seu banco principal.")

        
    # Gráfico visual dos KPIs expandido
    st.markdown("---")
    df_kpi = pd.DataFrame({
        "Indicador": [
            "Profit Share (%)", 
            "Índice de Principalidade (%)", 
            "Cross-sell (Prod/Cli)", 
            "Conversão Monoliner (%)", 
            "Wallet Diversificado (%)",
            "LTV / CAC",
            "NPS (Score)"
        ],
        "Atual": [35, 70, 2.1, 0, 10, 3.2, 72],
        "Meta (3 Anos)": [45, 100, 3.5, 20, 40, 6.0, 75]
    })
    
    fig_kpi = go.Figure(data=[
        go.Bar(name='Atual', x=df_kpi['Atual'], y=df_kpi['Indicador'], orientation='h', marker_color=ITAU_BLUE, text=df_kpi['Atual'], textposition='auto'),
        go.Bar(name='Meta (3 Anos)', x=df_kpi['Meta (3 Anos)'], y=df_kpi['Indicador'], orientation='h', marker_color=ITAU_ORANGE, text=df_kpi['Meta (3 Anos)'], textposition='auto')
    ])
    fig_kpi.update_traces(textfont_color='white', texttemplate='%{text}')
    fig_kpi.update_layout(
        barmode='group', 
        title="Evolução Esperada dos KPIs Críticos (Projetado)", 
        margin=dict(t=40, b=10, l=10, r=20), 
        height=450,
        yaxis={'categoryorder':'total ascending'}
    )
    st.plotly_chart(fig_kpi, use_container_width=True)


# --- PÁGINA 8: INFLUÊNCIA TRANSVERSAL BASEADA em DADOS ---
elif page == "8. Influência Transversal Baseada em Dados":
    st.title("📊 8. Influência Transversal Baseada em Dados")
    st.markdown("---")

    
    t1, t2 = st.tabs(["Influência", "Rituais de Performance"])
    
    with t1:
        st.write("")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='defense-box' style='border-left-color: #003399;'><h4>Produtos<br>(Crédito, Investimentos, Seguros)</h4><p>Utilizarei a evidência da sub-penetração de 10% em Investimentos para co-desenvolver produtos especializados que capturem a liquidez de específicos públicos, como Celebridades e da Média Renda, equilibrando o mix de receita.</p></div>", unsafe_allow_html=True)

        with c2:
            st.markdown("<div class='defense-box' style='border-left-color: #EC7000;'><h4>Canais e CRM</h4><p>Direcionarei os esforços de comunicação focando no potencial de conversão dos 1,5M de monoliners, demonstrando o ganho marginal de receita ao transformá-los em correntistas.</p></div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='defense-box' style='border-left-color: #333333;'><h4>Operações</h4><p>Será alinhado a necessidade de digitalização da jornada para otimizar os R$ 2,499 bilhões em custos operacionais, garantindo que o custo de servir seja compatível com a rentabilidade de cada segmento.</p></div>", unsafe_allow_html=True)

    with t2:
        st.write("")
        st.info("**Serão estabelecidos rituais mensais de performance focados em indicadores que refletem a saúde estratégica e a geração de valor:**")
        
        st.write("")
        ca1, ca2, ca3, ca4 = st.columns(4)
        with ca1:
            st.markdown("<div class='defense-box' style='height: 100%; border-left: none; border-top: 4px solid #003399;'><h4>Evolução do Profit Share</h4><p style='font-size: 13px;'>Monitoramento do crescimento da nossa fatia de lucro frente ao mercado (atualmente em 35%).</p></div>", unsafe_allow_html=True)
        with ca2:
            st.markdown("<div class='defense-box' style='height: 100%; border-left: none; border-top: 4px solid #EC7000;'><h4>Índice de Principalidade</h4><p style='font-size: 13px;'>Percentual da base com vínculo de recebimento (foco em elevar os atuais 1,4M de clientes).</p></div>", unsafe_allow_html=True)
        with ca3:
            st.markdown("<div class='defense-box' style='height: 100%; border-left: none; border-top: 4px solid #003399;'><h4>Eficiência Operacional</h4><p style='font-size: 13px;'>Relação custo/receita para garantir a sustentabilidade do P&L.</p></div>", unsafe_allow_html=True)
        with ca4:
            st.markdown("<div class='defense-box' style='height: 100%; border-left: none; border-top: 4px solid #EC7000;'><h4>NPS Segmentado</h4><p style='font-size: 13px;'>Garantia de que o adensamento está gerando valor percebido e satisfação.</p></div>", unsafe_allow_html=True)


# --- PÁGINA 9: VISIONING (IMPACTO) ---
elif page == "9. Visioning: Impacto":
    st.title("🌟 9. Visioning: Impacto em 1 Ano")
    st.markdown("---")
    
    # LINHA 1: Principalidade
    r1_col1, r1_col2 = st.columns(2)
    with r1_col1:
        st.markdown("<div class='defense-box' style='min-height: 260px; border-left-color: #003399;'><h4>Expansão e Ativação da Principalidade</h4><ul><li><b>Conversão de Monoliners:</b> Meta de converter 20% dos monoliners (300 mil clientes) em correntistas com vínculo de recebimento.</li><li><b>Ativação da Base de Correntistas:</b> Conversão de 20% do gap de principalidade (400 mil clientes) dos 2M de correntistas secundários para o status de clientes principais.</li><li><b>Objetivo:</b> Elevar o número de clientes com \"vínculo de recebimento no Itaú\" de 1,4 milhão para 2,1 milhões (incremento total de 700 mil novos clientes principais).</li></ul></div>", unsafe_allow_html=True)
    with r1_col2:
        df_1 = pd.DataFrame({"Cenário": ["Atual", "Projetado"], "Clientes (M)": [1.4, 2.1]})
        f1 = px.bar(df_1, x='Cenário', y='Clientes (Milhões)', title="Vínculo de Recebimento (Clientes Principais)", text_auto=True, color='Cenário', color_discrete_map={"Atual": ITAU_BLUE, "Projetado": ITAU_ORANGE}, height=260)
        f1.update_traces(textposition='inside', textfont_color='white')
        f1.update_layout(showlegend=False, margin=dict(l=10, r=10, t=35, b=10))
        st.plotly_chart(f1, use_container_width=True)


    # LINHA 2: Receita
    r2_col1, r2_col2 = st.columns(2)
    with r2_col1:
        st.markdown("<div class='defense-box' style='min-height: 240px; border-left-color: #EC7000;'><h4>Impacto no P&L e Profit Share</h4><ul><li><b>Crescimento de Receita:</b> Incremento projetado de ~14% (R$ 600M), elevando o resultado total para R$ 4,9 bilhões, impulsionado pela captura de investimentos e seguros que hoje estão na concorrência.</li><li><b>Salto no Profit Share:</b> Elevação do indicador de 35% para 45%, refletindo o sucesso em capturar uma fatia maior do valor total gerado pelo cliente no mercado.</li></ul></div>", unsafe_allow_html=True)
    with r2_col2:
        df_2 = pd.DataFrame({"Cenário": ["Atual", "Projetado"], "Receita (R$ Bi)": [4.3, 4.9]})
        f2 = px.bar(df_2, x='Cenário', y='Receita (R$ Bi)', title="Crescimento de Receita", text_auto=True, color='Cenário', color_discrete_map={"Atual": ITAU_BLUE, "Projetado": ITAU_ORANGE}, height=240)
        f2.update_traces(textposition='inside', textfont_color='white')
        f2.update_layout(showlegend=False, margin=dict(l=10, r=10, t=35, b=10))
        st.plotly_chart(f2, use_container_width=True)

    # LINHA 3: Eficiência
    r3_col1, r3_col2 = st.columns(2)
    with r3_col1:
        st.markdown("<div class='defense-box' style='min-height: 240px; border-left-color: #003399;'><h4>Eficiência de Escala</h4><ul><li>Aumento da margem de contribuição por cliente devido ao baixo custo marginal de servir um cliente já adensado, otimizando a estrutura de R$ 2,499 bilhões de custos operacionais.</li></ul></div>", unsafe_allow_html=True)
    with r3_col2:
        df_3 = pd.DataFrame({"Cenário": ["Atual", "Projetado"], "Profit Share (%)": [35, 45]})
        f3 = px.bar(df_3, x='Cenário', y='Profit Share (%)', title="Evolução do Profit Share", text_auto=True, color='Cenário', color_discrete_map={"Atual": ITAU_BLUE, "Projetado": ITAU_ORANGE}, height=240)
        f3.update_traces(textposition='inside', textfont_color='white')
        f3.update_layout(showlegend=False, margin=dict(l=10, r=10, t=35, b=10))
        st.plotly_chart(f3, use_container_width=True)

    st.success("**Resultado esperado**: Incremento de ~14% na receita, adicionando cerca de R$ 600M ao P&L, com melhoria substancial no Profit Share para 45%.")


# --- PÁGINA 10: FRAME MENTAL ---
elif page == "10. Frame Mental":

    st.title("🧠 10. Frame Mental - Estratégico (Matriz BCG)")
    st.markdown("---")
    
    html_timeline = """
<div style="position: relative; padding-left: 30px; margin-top: 10px;">
<!-- Linha vertical do tempo -->
<div style="position: absolute; left: 10px; top: 0; bottom: 0; width: 4px; background-color: #EC7000; border-radius: 2px;"></div>
<div class='defense-box' style='margin-bottom: 20px; border-left-color: #003399; position: relative;'>
<div style="position: absolute; left: -25px; top: 25px; width: 12px; height: 12px; background-color: #003399; border-radius: 50%; border: 2px solid white;"></div>
<h4 style='color: #003399; margin-bottom: 5px;'>Passo 1: Mapeamento e Diagnóstico (Data Intelligence)</h4>
<ul style='margin-top: 0;'>
<li><b>Ação:</b> Segmentação granular da base interna de 5MM de CPFs (Monoliners vs. Secundários vs. Principais) e cruzamento com o mercado potencial de 16,9MM de influenciadores.</li>
<li><b>Foco:</b> Mapear a "fuga de valor" de 65% do Profit Share, identificando com precisão em quais perfis e produtos a concorrência está capturando a liquidez de clientes que já possuem relacionamento com o Itaú.</li>
</ul>
</div>
<div class='defense-box' style='margin-bottom: 20px; border-left-color: #003399; position: relative;'>
<div style="position: absolute; left: -25px; top: 25px; width: 12px; height: 12px; background-color: #003399; border-radius: 50%; border: 2px solid white;"></div>
<h4 style='color: #003399; margin-bottom: 5px;'>Passo 2: Segmentação e Proposta de Valor (Customer Centricity)</h4>
<ul style='margin-top: 0;'>
<li><b>Ação:</b> Clusterizar a base em Baixa, Média e Alta Renda.</li>
<li><b>Foco:</b> Definir o que cada um precisa: educação financeira para o Nano ou gestão de fortuna para a Celebridade.</li>
</ul>
</div>
<div class='defense-box' style='margin-bottom: 20px; border-left-color: #003399; position: relative;'>
<div style="position: absolute; left: -25px; top: 25px; width: 12px; height: 12px; background-color: #003399; border-radius: 50%; border: 2px solid white;"></div>
<h4 style='color: #003399; margin-bottom: 5px;'>Passo 3: Priorização e Alavancas (Business Case)</h4>
<ul style='margin-top: 0;'>
<li><b>Ação:</b> Seleção de batalhas com foco em ROI de curto prazo: Priorização do adensamento dos 2MM de correntistas secundários (ativação de principalidade) e conversão dos 1,5MM monoliners (migração para conta).</li>
<li><b>Foco:</b> Direcionar o esforço de implementação onde o CAC (Custo de Aquisição) é marginal zero, garantindo o maior retorno imediato para o P&L e a sustentabilidade do LAIR através da principalidade.</li>
</ul>
</div>
<div class='defense-box' style='margin-bottom: 20px; border-left-color: #003399; position: relative;'>
<div style="position: absolute; left: -25px; top: 25px; width: 12px; height: 12px; background-color: #003399; border-radius: 50%; border: 2px solid white;"></div>
<h4 style='color: #003399; margin-bottom: 5px;'>Passo 4: Implementação e Influência (Test & Learn)</h4>
<ul style='margin-top: 0;'>
<li><b>Ação:</b> Engajar parceiros de Produto e CRM para lançar pilotos (MVPs).</li>
<li><b>Foco:</b> Criar a jornada de isenção por "publis" ou a integração PF+PJ.</li>
</ul>
</div>
<div class='defense-box' style='margin-bottom: 20px; border-left-color: #003399; position: relative;'>
<div style="position: absolute; left: -25px; top: 25px; width: 12px; height: 12px; background-color: #003399; border-radius: 50%; border: 2px solid white;"></div>
<h4 style='color: #003399; margin-bottom: 5px;'>Passo 5: Monitoramento e Ajuste (Governance)</h4>
<ul style='margin-top: 0;'>
<li><b>Ação:</b> Acompanhar os indicadores estratégicos (Profit Share, Principalidade, NPS).</li>
<li><b>Foco:</b> Reportar ao Board e ajustar a rota para garantir o crescimento de ~14% ao ano.</li>
</ul>
</div>
</div>
"""
    st.markdown(html_timeline, unsafe_allow_html=True)


# --- PÁGINA 11: PRODUTOS E SERVIÇOS ---
elif page == "11. Produtos e Serviços":
    st.markdown("<h3 style='margin-bottom: 0px; padding-bottom: 5px; margin-top: 0px;'>🛠️ 11. Produtos e Serviços</h3>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 0px 0px 10px 0px;'>", unsafe_allow_html=True)
    
    st.markdown("Catálogo de produtos aplicados para estruturação do Case: **Itaú o Banco do Influencer**.")


    
    cards_html = """
<div class='defense-box' style='margin-bottom: 20px; border-left-color: #EC7000;'>
<h4 style='color: #EC7000; margin-bottom: 5px;'>Itaú Emps e Superapp (Integração PF+PJ)</h4>
<p style='margin-top: 0;'>Essencial para o segmento de Média Renda. Use para defender a migração de Pessoa Física para Jurídica, facilitando o recebimento de contratos de agências.</p>
</div>

<div class='defense-box' style='margin-bottom: 20px; border-left-color: #003399;'>
<h4 style='color: #003399; margin-bottom: 5px;'>Vínculo de Recebimento (Domicílio Bancário)</h4>
<p style='margin-top: 0;'>Ferramenta central para converter os 1,5M de monoliners e garantir que o faturamento do influenciador nasça no Itaú.</p>
</div>

<div class='defense-box' style='margin-bottom: 20px; border-left-color: #333333;'>
<h4 style='color: #333333; margin-bottom: 5px;'>Itaú Private (Influencer Desk)</h4>
<p style='margin-top: 0;'>Serviço exclusivo para a Alta Renda. Demonstra conhecimento em gestão de grandes fortunas e planejamento sucessório.</p>
</div>

<div class='defense-box' style='margin-bottom: 20px; border-left-color: #EC7000;'>
<h4 style='color: #EC7000; margin-bottom: 5px;'>Previdência e Investimentos</h4>
<p style='margin-top: 0;'>Soluções para elevar a receita de 10% nesta linha, focando no conceito de "carreiras de ciclo curto".</p>
</div>

<div class='defense-box' style='margin-bottom: 20px; border-left-color: #003399;'>
<h4 style='color: #003399; margin-bottom: 5px;'>Seguros de Imagem e Lucros Cessantes</h4>
<p style='margin-top: 0;'>Produtos de proteção patrimonial que ajudam a elevar a participação de 20% de seguros no P&L.</p>
</div>

<div class='defense-box' style='margin-bottom: 20px; border-left-color: #333333;'>
<h4 style='color: #333333; margin-bottom: 5px;'>Microcrédito Orientado</h4>
<p style='margin-top: 0;'>Focado no segmento Nano, para financiar equipamentos e impulsionar a profissionalização desde o início.</p>
</div>
"""
    st.markdown(cards_html, unsafe_allow_html=True)

# --- PÁGINA 12: AGRADECIMENTO ---
elif page == "12. Agradecimento":
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='text-align: center;'>
            <h1 style='color: {ITAU_ORANGE}; font-size: 48px; margin-bottom: 20px;'>Obrigado pela Atenção!</h1>
            <p style='font-size: 20px; color: {ITAU_BLUE}; max-width: 800px; margin: 0 auto;'>
                Agradeço a oportunidade de apresentar o <b>Case: Itaú o Banco do Influencer</b>.
            </p>
            <br>
            <p style='font-size: 18px; color: #555;'>Estou à disposição para os próximos passos.</p>
            <hr style='width: 100px; margin: 40px auto; border-top: 3px solid {ITAU_ORANGE};'>
        </div>

    """, unsafe_allow_html=True)
    st.balloons()




