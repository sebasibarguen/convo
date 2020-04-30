window.onload = function() {

    let timeout = null;

    const inputEventListener = () => {
        clearTimeout(timeout);

        timeout = setTimeout(function () {
            listenToWords()
        }, 1000);
    }

    const listenToWords = async (e) => {

        let trix = document.querySelector("trix-editor")
        let suggestionElement = document.getElementById("suggestion")

        let text = trix.editor.getDocument().toString()
        let words = text.trim().split(" ")

        let suggetedText = [];
        let result;
        for (let i in words) {
            result = await matches(words[i])
            console.log(result)
            if (result.includes(words[i])) {
                suggetedText.push(words[i])
            } else {
                suggetedText.push(result[0])
            }
        }
        
        suggestionElement.innerHTML = suggetedText.join(" ")
    }
    
    
    const matches = async (word) => {
        const response = await fetch('/api?keyword=' + word)
        const matches = await response.json()

        let suggestions = matches['suggestions'].map(m => m[1])
        return suggestions
    }

    document.querySelector("trix-editor").addEventListener('trix-change', inputEventListener)
};