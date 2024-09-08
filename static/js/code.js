document.getElementById('generate-pdf').addEventListener('click', function() {
    const option = document.getElementById('select-option').value;
    // Redirige vers la vue Django pour générer le fichier PDF
    window.location.href = `/reports/generate-pdf/?option=${option}`;
});

document.getElementById('generate-excel').addEventListener('click', function() {
    const option = document.getElementById('select-option').value;
    // Redirige vers la vue Django pour générer le fichier Excel
    window.location.href = `/reports/generate-excel/?option=${option}`;
});
