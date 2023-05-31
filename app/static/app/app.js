document.addEventListener('DOMContentLoaded', function () {

    // load
    const data = JSON.parse(document.querySelector('#data').innerHTML);
    //console.log(typeof (data));
    let words = data.words;
    let translation = data.translation;
    let sentences = data.sentences;
    let value = data.value;
    console.log(words);
    console.log(translation);
    console.log(sentences);
    console.log(value);





    //functions
    function refresh() {
        if (words.length === 0) {
            document.querySelector('#finish').submit();
        }
        document.querySelector('#text').innerHTML = words[0];

        document.querySelector('#sentence').innerHTML = '';
        document.querySelector('#footer').innerHTML = `剩余：${words.length}`;
        document.querySelector('#allButtons').style.display = 'none';
        document.querySelector('#translate').style.display = '';

    }
    function show(d) {
        let days = [0, 1, 2, 7, 14];
        document.querySelector('#allButtons').style.display = '';
        days.forEach(function (currentValue) {
            if (currentValue === d) {
                document.querySelector(`#day${currentValue}`).style.display = '';
            } else {
                document.querySelector(`#day${currentValue}`).style.display = 'none';
            }
            //console.log('triggered');
        })

    }


    function translate() {


        document.querySelector('#text').innerHTML = translation[0];
        document.querySelector('#sentence').innerHTML = sentences[0];


        show(value[0]);
        document.querySelector('#translate').style.display = 'none';
    }
    //initialize

    refresh();

    let inputs = document.querySelectorAll('input')

    for (let i = 0; i < inputs.length; i++) {
        inputs[i].onclick = (ev) => {
            if (inputs[i].dataset.value == 0) {
                let w = words[0];
                let trans = translation[0];
                let s = sentences[0];
                words.push(w);
                translation.push(trans);
                sentences.push(s);
                value.push(0)
            }
            console.log(ev.target.getAttribute('data-value'));
            console.log(123);
            document.querySelector('#save').setAttribute('value', `${ev.target.getAttribute('data-value')},${words[0]}`);

            words.splice(0, 1);
            translation.splice(0, 1);
            sentences.splice(0, 1);
            value.splice(0, 1);

            refresh();
        }










        // translate button
        document.querySelector('#translate').onclick = (ev) => {
            translate();
            ev.stopPropagation();
        };


        document.querySelector('#pronounce').onclick = (ev) => {
            var audio = new Audio(`https://api.frdic.com/api/v2/speech/speakweb?langid=de&txt=${words[0]}`);
            audio.play();
            ev.stopPropagation();

        }


    }


})