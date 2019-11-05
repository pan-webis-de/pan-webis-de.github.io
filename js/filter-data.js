if (document.location.hash.startsWith("#filter:")) {
    const query = decodeURIComponent(document.location.hash.substr(8));
    document.location.hash = "#?q=" + query;
}

initFiltering(".targetable", "tbody tr", entry => {
    const attributes = entry.dataset;
    attributes['name'] = entry.children[1].textContent.toLowerCase().replace(/[^\x20-\x7E]/g, '');
    attributes['year'] = entry.children[3].textContent;
    attributes['task'] = entry.children[6].textContent.toLowerCase().replace(/[^\x20-\x7E]/g, '');
    return attributes;
});