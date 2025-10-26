const selected = new Set();
const compareButton = document.getElementById('compare-button');
const productButtons = document.querySelectorAll('.compare-select');
const homeButton = document.getElementById('home-button');

productButtons.forEach(btn => {
btn.addEventListener('click', () => {
    const sku = btn.dataset.sku;
    if (selected.has(sku)) {
    selected.delete(sku);
    btn.textContent = 'Select for Compare';
    btn.classList.remove('bg-green-500');
    btn.classList.add('bg-blue-500');
    } else {
    if (selected.size < 2) {
        selected.add(sku);
        btn.textContent = 'Selected';
        btn.classList.remove('bg-blue-500');
        btn.classList.add('bg-green-500');
    } else {
        alert('You can only compare 2 guitars at once.');
    }
    }

    if (selected.size === 2) {
    compareButton.disabled = false;
    compareButton.classList.remove('bg-gray-400', 'cursor-not-allowed');
    compareButton.classList.add('bg-red-500', 'cursor-pointer');
    } else {
    compareButton.disabled = true;
    compareButton.classList.add('bg-gray-400', 'cursor-not-allowed');
    compareButton.classList.remove('bg-red-500', 'cursor-pointer');
    }
});
});

compareButton.addEventListener('click', () => {
if (selected.size === 2) {
    const ids = Array.from(selected).join(',');
    window.location.href = `/guitarguitar/compareTwoProducts/?ids=${ids}`;
    }
});

homeButton.addEventListener('click', () => {
    window.location.href = `/guitarguitar/index/`;
});