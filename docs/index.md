<section class="agent-hero">
  <div class="agent-hero__content">
    <p class="agent-eyebrow">Legal data infrastructure for agentic workflows</p>
    <h1>Dados judiciais públicos, prontos para automações jurídicas confiáveis.</h1>
    <p class="agent-lede">
      <strong>esaj-datajud</strong> é um toolkit Python para consultar, estruturar e auditar dados públicos do
      eSAJ/TJSP e comunicações DJEN/DataJud com rastreabilidade, testes e governança.
    </p>
    <div class="agent-actions">
      <a class="agent-button agent-button--primary" href="quickstart/">Começar agora</a>
      <a class="agent-button" href="https://github.com/lucmolero/esaj-datajud">Ver no GitHub</a>
    </div>
  </div>
  <div class="agent-hero__visual" aria-label="Fluxo visual de agentes jurídicos">
    <div class="agent-console">
      <div class="agent-console__bar">
        <span></span><span></span><span></span>
      </div>
      <div class="agent-console__body">
        <div class="agent-step agent-step--active">
          <strong>ingest</strong>
          <span>CNJ validado</span>
        </div>
        <div class="agent-path"></div>
        <div class="agent-step">
          <strong>parse</strong>
          <span>partes + movimentos</span>
        </div>
        <div class="agent-path"></div>
        <div class="agent-step">
          <strong>audit</strong>
          <span>JSON rastreável</span>
        </div>
        <pre><code>{
  "status": "ok",
  "fonte": "eSAJ/TJSP",
  "movimentacoes": 10310,
  "coverage": "90%+"
}</code></pre>
      </div>
    </div>
  </div>
</section>

<section class="agent-trust-grid" aria-label="Indicadores de confiança">
  <article>
    <strong>90%+</strong>
    <span>cobertura automatizada</span>
  </article>
  <article>
    <strong>CI</strong>
    <span>Python 3.10, 3.11 e 3.12</span>
  </article>
  <article>
    <strong>CodeQL</strong>
    <span>análise de segurança contínua</span>
  </article>
  <article>
    <strong>LGPD</strong>
    <span>uso responsável documentado</span>
  </article>
</section>

## Para Quem É

<div class="agent-card-grid">
  <article>
    <h3>Advocacia</h3>
    <p>Estruture consultas públicas recorrentes sem perder rastreabilidade ou depender de planilhas manuais.</p>
  </article>
  <article>
    <h3>Legaltech</h3>
    <p>Use uma base aberta, tipada e testada para construir produtos jurídicos com dados oficiais.</p>
  </article>
  <article>
    <h3>Pesquisa</h3>
    <p>Trabalhe com metodologia, reprodutibilidade, limites declarados e fixtures sanitizadas.</p>
  </article>
</div>

## Por Que Confiar

<div class="agent-proof">
  <div>
    <h3>Engenharia verificável</h3>
    <p>Testes sem rede, testes live opcionais, lint, type check, build, <code>twine check</code>, <code>pip-audit</code> e releases com artefatos públicos.</p>
  </div>
  <div>
    <h3>Domínio jurídico real</h3>
    <p>O parser cobre dados básicos, partes, movimentações, documentos, audiências, petições, incidentes, apensos e comunicações DJEN/DataJud.</p>
  </div>
  <div>
    <h3>Limites explícitos</h3>
    <p>O projeto não burla autenticação, senha, captcha, segredo de justiça ou restrições técnicas das fontes consultadas.</p>
  </div>
</div>

## Fluxo De Uso

```python
from esaj_datajud import EsajDatajudClient, EsajDatajudConfig

client = EsajDatajudClient(
    EsajDatajudConfig(
        timeout=20,
        rate_limit_interval=1.0,
        cache_enabled=True,
    )
)

extrato = client.get_extrato("1076539-20.2019.8.26.0100")
print(extrato["dados_basicos"]["classe"])
print(len(extrato["movimentacoes"]))
```

## Projeto Independente

`esaj-datajud` não é um produto oficial do TJSP, CNJ, eSAJ ou DataJud. A biblioteca organiza consultas a fontes públicas ou legitimamente acessíveis pelo usuário e foi desenhada para uso técnico e jurídico responsável.

<div class="agent-final-cta">
  <div>
    <h2>Comece pela rota curta.</h2>
    <p>Instale localmente, rode uma consulta e avance para o cliente configurável quando precisar de cache, rate limit e logging.</p>
  </div>
  <a class="agent-button agent-button--primary" href="quickstart/">Abrir quickstart</a>
</div>
