function quickSort(array) {
    // Если массив содержит 0 или 1 элемент, он уже отсортирован
    if (array.length <= 1) {
        return array;
    }

    // Выбираем опорный элемент (pivot)
    const pivot = array[array.length - 1]; // можно выбрать любой элемент
    const left = []; // Массив для элементов меньше опорного
    const right = []; // Массив для элементов больше опорного

    // Проходим по всем элементам массива, кроме опорного
    for (let i = 0; i < array.length - 1; i++) {
        if (array[i] < pivot) {
            left.push(array[i]); // Добавляем в левый массив
        } else {
            right.push(array[i]); // Добавляем в правый массив
        }
    }

    // Рекурсивно применяем быструю сортировку к левому и правому массивам и соединяем их с опорным элементом
    return [...quickSort(left), pivot, ...quickSort(right)];
}

// Пример использования
const unsortedArray = [34, 7, 23, 32, 5, 62];
const sortedArray = quickSort(unsortedArray);
console.log(sortedArray); // Вывод: [5, 7, 23, 32, 34, 62]

