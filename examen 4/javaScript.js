function analizarConsumo(consumos) {
    
    let diasAltos = 0;
    let total = 0;
    let minimo = consumos[0];

    for (let i = 0; i < consumos.length; i++) {
        
        if (consumos[i] > 30) {
            diasAltos++;
        }

        total += consumos[i];

        if (consumos[i] < minimo) {
            minimo = consumos[i];
        }
    }

    return [diasAltos, total, minimo];
}