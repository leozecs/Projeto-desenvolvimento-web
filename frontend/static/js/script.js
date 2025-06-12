// ==========================================
// SPA REDE VERMELHA - JavaScript
// ==========================================

document.addEventListener('DOMContentLoaded', () => {
  const conteudo = document.getElementById('conteudo');

  // =========================== //
  // Carrega uma página SPA      //
  // =========================== //
  function loadPage(pageName, addToHistory = true) {
    const path = `paginas/${pageName}.html`;

    // Evita recarregamento
    if (conteudo.getAttribute('data-current') === path) return;

    // Mostra loader
    conteudo.innerHTML = '<div class="loader">Carregando...</div>';

    fetch(path)
      .then(res => {
        if (!res.ok) throw new Error(`Erro ${res.status}: ${res.statusText}`);
        return res.text();
      })
      .then(html => {
        conteudo.innerHTML = html;
        conteudo.setAttribute('data-current', path);
        scrollToTop();
        highlightActiveLink(pageName);
        fadeInContent();

        if (addToHistory) {
          history.pushState({ page: pageName }, '', `#${pageName}`);
        }

        console.log(`[SPA] Página carregada: ${pageName}`);

        // Reexecuta scripts específicos
        if (pageName === 'formulario') initForm();
      })
      .catch(err => {
        conteudo.innerHTML = `
          <div style="padding: 40px; text-align: center;">
            <h2>Página não encontrada 😕</h2>
            <p>Verifique o endereço ou volte para a <a href="#" data-pagina="home">página inicial</a>.</p>
          </div>`;
        console.error(`[SPA] Falha ao carregar "${pageName}":`, err);
      });
  }

  // =============================== //
  // Ativa visualmente o menu atual //
  // =============================== //
  function highlightActiveLink(pageName) {
    const links = document.querySelectorAll('[data-pagina]');
    links.forEach(link => {
      const target = link.getAttribute('data-pagina');
      link.classList.toggle('active', target === pageName);
    });
  }

  // ================= //
  // Scroll ao topo    //
  // ================= //
  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // ============================ //
  // Animação de fade-in no load //
  // ============================ //
  function fadeInContent() {
    conteudo.style.opacity = 0;
    conteudo.style.transition = 'opacity 0.3s ease';
    requestAnimationFrame(() => {
      conteudo.style.opacity = 1;
    });
  }

  // =========================================== //
  // Inicializa a primeira página (via hash URL) //
  // =========================================== //
  const initialPage = window.location.hash.slice(1) || 'home';
  loadPage(initialPage, false);

  // ========================================= //
  // Clique no menu principal (nav a[data-pagina])
  // ========================================= //
  document.querySelectorAll('nav a[data-pagina]').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const destino = link.getAttribute('data-pagina');
      if (destino) loadPage(destino);
    });
  });

  // =============================================== //
  // Clique em qualquer botão/link SPA do site       //
  // =============================================== //
  document.body.addEventListener('click', e => {
    const link = e.target.closest('[data-pagina]');
    if (link && link.tagName === 'A') {
      e.preventDefault();
      const destino = link.getAttribute('data-pagina');
      if (destino) loadPage(destino);
    }
  });

  // =========================================== //
  // Botão "Voltar" do navegador (history API)   //
  // =========================================== //
  window.addEventListener('popstate', event => {
    const page = event.state?.page || 'home';
    loadPage(page, false);
  });

  // ================================================= //
  // Inicialização do formulário                      //
  // ================================================= //
  function initForm() {
    const form = document.getElementById('form-doacao');
    const mensagem = document.getElementById('mensagem');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      mensagem.innerHTML = '';

      const formData = new FormData(form);
      const dados = {};
      let camposInvalidos = [];

      formData.forEach((value, key) => {
        const input = form.querySelector(`[name="${key}"]`);
        const valor = value.trim();

        // Campos opcionais
        const opcionais = ['detalhe_medicacao', 'qual_doenca'];

        if (key === 'termos') {
          if (input && input.checked) {
            dados[key] = 1;
          } else {
            camposInvalidos.push('Você precisa aceitar os termos.');
          }
        } else if (opcionais.includes(key)) {
          dados[key] = valor; // sem validação obrigatória
        } else {
          dados[key] = valor;
          if (!valor) {
            camposInvalidos.push(`Campo obrigatório: ${key.replaceAll('_', ' ')}`);
          }
        }
      });

      if (camposInvalidos.length > 0) {
        mensagem.innerHTML = `<p style="color:red;">❌ ${camposInvalidos.join('<br>')}</p>`;
        return;
      }

      try {
        const resposta = await fetch('http://localhost:5000/api/doadores', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(dados)
        });

        const resultado = await resposta.json();

        if (resposta.ok) {
          mensagem.innerHTML = `<p style="color:green;">✅ ${resultado.mensagem}</p>`;
          form.reset();

          // Redireciona para página de agradecimento após sucesso
          setTimeout(() => {
            loadPage('obrigado');
          }, 1200);
        } else {
          mensagem.innerHTML = `<p style="color:red;">❌ ${resultado.erros?.join('<br>') || resultado.erro}</p>`;
        }
      } catch (erro) {
        mensagem.innerHTML = `<p style="color:red;">Erro ao conectar com o servidor.</p>`;
      }
    });
  }

  document.addEventListener('click', function (e) {
  if (e.target.classList.contains('ver-mais')) {
    const depoimento = e.target.closest('.depoimento');
    depoimento.classList.toggle('expanded');
    e.target.textContent = depoimento.classList.contains('expanded') ? 'Ver menos' : 'Ver mais';
  }
});

});
