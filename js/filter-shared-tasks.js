if (document.location.hash.startsWith("#filter:")) {
    const query = decodeURIComponent(document.location.hash.substr(8));
    document.location.hash = "#?q=" + query;
}

initFiltering(".targetable", "tbody tr", entry => {
    const attributes = entry.dataset;
    attributes['name'] = entry.children[1].textContent.toLowerCase();
    attributes['task'] = entry.children[2].textContent.toLowerCase();
    attributes['edition'] = entry.children[3].textContent;
    return attributes;
});