search = () => {
    let query = document.getElementById('searchField').value;
    console.log(query);
    document.getElementById('cont').classList.add('colorful');
    document.getElementById('list').innerHTML = `
    <div class="list-load"></div>
    <div class="list-load reverse"></div>
    `;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost:3000/search', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function (ev) {
        document.getElementById('list').innerHTML = '';
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            let list = JSON.parse(this.response);
            console.log(list);
            let finalTemplate = `<div class="list-title">
            <p>Results..</p>
        </div>`;
            list.forEach(movie => {
                let genreTemplate = ''
                movie.Genre.forEach(genre => {
                    if (genre) {
                        genreTemplate += `<p>${genre}</p>`
                    }
                });
                let template = `  
        <div class="movie">
        <div class="title">
          <p>
            ${movie.Title}
          </p>
        </div>
        <div class="genre">
          ${genreTemplate}
        </div>
        <div class="references">
          <p>
            Have a look on
            <span><a target="_blank" href="https://www.imdb.com/title/tt${movie.imdbId}">IMDB</a></span>
          </p>
        </div>
        <div class="rating">
          <p>Rating: ${movie.Rating}</p>
        </div>
      </div>
                `;
                finalTemplate += template;
                document.getElementById('list').innerHTML = finalTemplate;
            });
        } else if (this.readyState === XMLHttpRequest.DONE && this.status === 400) {
            console.log(this.response)
        }
        document.getElementById('cont').classList.remove('colorful');
    }
    xhr.send(JSON.stringify({ query: query }));
}