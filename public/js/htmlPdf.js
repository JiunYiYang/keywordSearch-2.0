window.onload = function() {

    document.getElementById('btn-htmlPdf').onclick = function() {

        html2canvas(document.getElementById('content')).then(function (canvas) {

            background: '#FFFFFF';

            var imgData = canvas.toDataURL('image/jpeg');
            var doc = new jsPDF('p', 'mm', 'a4');

            doc.addImage(imgData, 'JPEG', 0, 0, 210, 297);
            doc.save('content.pdf');
        });
    }
}


