search = () => {
    let query = document.getElementById('searchField').value;
    console.log(query);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost:3000/search', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function (ev) {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            console.log(this.response);
        }
    }
    xhr.send(JSON.stringify({ query: query }));
}