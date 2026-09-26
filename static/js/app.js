document.addEventListener('DOMContentLoaded', () => {
    const modalEl = document.getElementById('modalEditarTarefa');
    let editModalInstance = null;
    if (modalEl && typeof bootstrap !== 'undefined') {
        editModalInstance = new bootstrap.Modal(modalEl);
    }

    window.abrirModalEdicao = function (id, titulo, descricao, categoriaId, prioridade, dataLimite) {
        const form = document.getElementById('formModalEdicao');
        const inputTitulo = document.getElementById('modalEditTitulo');
        const inputDescricao = document.getElementById('modalEditDescricao');
        const selectCategoria = document.getElementById('modalEditCategoria');
        const selectPrioridade = document.getElementById('modalEditPrioridade');
        const inputDataLimite = document.getElementById('modalEditDataLimite');

        if (!form) return;

        form.action = `/tarefas/${id}/editar/`;
        if (inputTitulo) inputTitulo.value = titulo || '';
        if (inputDescricao) inputDescricao.value = descricao || '';
        if (selectCategoria) selectCategoria.value = categoriaId || '';
        if (selectPrioridade) selectPrioridade.value = prioridade || 'media';
        if (inputDataLimite) inputDataLimite.value = dataLimite || '';

        if (editModalInstance) {
            editModalInstance.show();
        } else if (modalEl) {
            const bsModal = bootstrap.Modal.getOrCreateInstance(modalEl);
            bsModal.show();
        }
    };

    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alertEl => {
        setTimeout(() => {
            if (typeof bootstrap !== 'undefined') {
                const bsAlert = bootstrap.Alert.getOrCreateInstance(alertEl);
                if (bsAlert) {
                    bsAlert.close();
                }
            }
        }, 4500);
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            const searchInput = document.querySelector('input[name="q"]');
            if (searchInput) {
                e.preventDefault();
                searchInput.focus();
            }
        }
    });
});
