---
hide:
  - navigation
  - toc
---

<main class="legal-home">
  <section class="legal-hero" aria-labelledby="legal-home-title">
    <div class="legal-hero__copy">
      <div class="legal-brandline">
        <img src="assets/logo.svg" alt="" />
        <span>esaj-datajud</span>
      </div>
      <p class="legal-kicker">Open source legal data infrastructure</p>
      <h1 id="legal-home-title">Dados judiciais públicos para agentes, automações e pesquisa jurídica confiável.</h1>
      <p class="legal-lede">
        Uma biblioteca Python para consultar, estruturar e auditar informações públicas do eSAJ/TJSP, dados
        estruturados do DataJud/CNJ e comunicações do DJEN com rastreabilidade, testes automatizados e governança
        documentada.
      </p>
      <div class="legal-actions" aria-label="Ações principais">
        <a class="legal-button legal-button--primary" href="quickstart/">Começar pelo quickstart</a>
        <a class="legal-button" href="api-reference/">Explorar API</a>
        <a class="legal-button legal-button--ghost" href="https://github.com/lucmolero/esaj-datajud">GitHub</a>
      </div>
    </div>

    <div class="legal-hero__system" aria-label="Fluxo técnico de dados jurídicos">
      <div class="legal-system__top">
        <span class="legal-dot legal-dot--green"></span>
        <span>agentic legal pipeline</span>
      </div>
      <div class="legal-flow">
        <div class="legal-node">
          <strong>01</strong>
          <span>CNJ validado</span>
        </div>
        <div class="legal-connector"></div>
        <div class="legal-node">
          <strong>02</strong>
          <span>Fonte pública</span>
        </div>
        <div class="legal-connector"></div>
        <div class="legal-node legal-node--active">
          <strong>03</strong>
          <span>JSON auditável</span>
        </div>
      </div>
      <pre><code>{
  "tribunal": "TJSP",
  "origem": "eSAJ",
  "status": "estruturado",
  "governanca": ["LGPD", "limites", "reprodutibilidade"],
  "automacao": "pronta_para_agentes"
}</code></pre>
    </div>
  </section>

  <section class="legal-signal-grid" aria-label="Sinais de confiança do projeto">
    <article>
      <strong>90%+</strong>
      <span>cobertura automatizada</span>
    </article>
    <article>
      <strong>Typed</strong>
      <span>contratos públicos e <code>py.typed</code></span>
    </article>
    <article>
      <strong>CI + CodeQL</strong>
      <span>qualidade e segurança contínuas</span>
    </article>
    <article>
      <strong>LGPD</strong>
      <span>uso responsável documentado</span>
    </article>
  </section>

  <section class="legal-section legal-section--split">
    <div>
      <p class="legal-section__eyebrow">Para quem está construindo o futuro jurídico</p>
      <h2>Base técnica para produtos, escritórios e pesquisa aplicada.</h2>
    </div>
    <p>
      O projeto foi desenhado para unir engenharia de software, responsabilidade jurídica e abertura acadêmica. Ele
      transforma consultas públicas em dados estruturados para fluxos verificáveis, sem prometer acesso privilegiado,
      contornar barreiras ou substituir análise profissional.
    </p>
  </section>

  <section class="legal-card-grid" aria-label="Casos de uso">
    <article>
      <span class="legal-card__label">Advocacia</span>
      <h3>Rotinas repetíveis</h3>
      <p>Consulta, estruturação e extração de informações públicas para reduzir retrabalho operacional.</p>
    </article>
    <article>
      <span class="legal-card__label">Legaltech</span>
      <h3>Produto sobre base aberta</h3>
      <p>Contratos tipados, cliente configurável, cache opt-in e erros previsíveis para integração profissional.</p>
    </article>
    <article>
      <span class="legal-card__label">Academia</span>
      <h3>Metodologia explícita</h3>
      <p>Documentação sobre reprodutibilidade, fixtures sanitizadas, limitações e validação controlada.</p>
    </article>
  </section>

  <section class="legal-section legal-section--accent">
    <div>
      <p class="legal-section__eyebrow">Engenharia verificável</p>
      <h2>Um projeto open source que mostra senioridade no código e no cuidado institucional.</h2>
      <p>
        O repositório combina parser, cliente, CLI, documentação, testes sem rede, testes live opcionais, validação de
        build, auditoria de dependências, changelog, governança, segurança e notas de release versionadas.
      </p>
    </div>
    <div class="legal-checklist" aria-label="Camadas de qualidade">
      <span>Testes automatizados</span>
      <span>Type checking</span>
      <span>Lint e formatação</span>
      <span>Build validado</span>
      <span>Threat model</span>
      <span>Uso responsável</span>
    </div>
  </section>

  <section class="legal-code-section" aria-labelledby="legal-code-title">
    <div>
      <p class="legal-section__eyebrow">Primeiro uso</p>
      <h2 id="legal-code-title">Instale, consulte e trabalhe com dados estruturados.</h2>
      <p>
        A API favorece fluxos claros: configurar limites, consultar uma fonte pública e receber um extrato pronto para
        auditoria, persistência ou integração com agentes internos.
      </p>
    </div>
    <pre><code>from esaj_datajud import EsajDatajudClient, EsajDatajudConfig

client = EsajDatajudClient(
    EsajDatajudConfig(
        timeout=20,
        rate_limit_interval=1.0,
        cache_enabled=True,
    )
)

extrato = client.get_extrato("1076539-20.2019.8.26.0100")
print(extrato["dados_basicos"]["classe"])
print(len(extrato["movimentacoes"]))</code></pre>
  </section>

  <section class="legal-footer-cta">
    <div>
      <p class="legal-section__eyebrow">Projeto independente</p>
      <h2>Pronto para avaliação técnica, uso responsável e evolução pública.</h2>
      <p>
        <strong>esaj-datajud</strong> não é um produto oficial do TJSP, CNJ, eSAJ ou DataJud. A biblioteca organiza
        consultas a fontes públicas ou legitimamente acessíveis pelo usuário.
      </p>
    </div>
    <div class="legal-actions">
      <a class="legal-button legal-button--primary" href="quickstart/">Abrir quickstart</a>
      <a class="legal-button" href="governanca/">Ver governança</a>
    </div>
  </section>
</main>
