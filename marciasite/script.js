function fetchGlossaryTerms() {
    fetch('http://127.0.0.1:8000/termos')
        .then(response => response.json())
        .then(data => {
            if (!data.termos || !Array.isArray(data.termos)) {
                console.error("Formato de dados inesperado:", data);
                return;
            }
            console.log(data.termos)
            const sortedTerms = data.termos
                .filter(term => term.nome)
                .sort((a, b) => a.nome.localeCompare(b.nome));

            const glossary = {};
            sortedTerms.forEach(term => {
                const firstLetter = term.nome.charAt(0).toUpperCase();
                if (!glossary[firstLetter]) {
                    glossary[firstLetter] = [];
                }
                glossary[firstLetter].push(term);
            });

            renderGlossary(glossary);
        })
        .catch(error => console.error("Erro ao buscar os termos:", error));
}

function renderGlossary(glossary) {
    const container = document.getElementById('glossary-container');
    container.innerHTML = '';

    for (const letter in glossary) {
        const section = document.createElement('div');
        section.classList.add('letter-section');
        
        const title = document.createElement('h2');
        title.classList.add('letter-title');
        title.textContent = letter;
        section.appendChild(title);
        
        const termList = document.createElement('ul');
        
        glossary[letter].forEach(term => {
            const item = document.createElement('li');
            item.classList.add('term-item');
            
            const termContent = document.createElement('div');
            termContent.innerHTML = `<span class="term-name">${term.nome}</span>: ${term.definicao || 'Definição não disponível'}`;
            
            for (const key in term) {
                if (key !== 'nome' && key !== 'definicao') {
                    const extraInfo = document.createElement('div');
                    extraInfo.classList.add('term-content');
                    extraInfo.textContent = `${key}: ${term[key]}`;
                    termContent.appendChild(extraInfo);
                }
            }
            
            item.appendChild(termContent);
            termList.appendChild(item);
        });
        
        section.appendChild(termList);
        container.appendChild(section);
    }
}

// Chama a função para buscar e exibir os termos do glossário
fetchGlossaryTerms();
