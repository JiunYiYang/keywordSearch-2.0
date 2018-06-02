window.onload = function() {

    document.getElementById('btn-htmlPdf').onclick = function() {
        document.getElementById('downloadSpin').style.display = 'block';

        html2canvas(document.getElementById('content')).then(function (canvas) {

            background: '#FFFFFF';

            var imgData = canvas.toDataURL('image/jpeg');
            var doc = new jsPDF('p', 'mm', [270, 520]);

            doc.addImage(imgData, 'JPEG', 10, 10, 250, 500);
            doc.save('content.pdf');
            document.getElementById('downloadSpin').style.display = 'none';
        });
    }
}


