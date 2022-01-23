function CopyToClipboard(){
    const e = document.getElementById("password-text")
    const copyText = e.innerHTML.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    navigator.clipboard.writeText(copyText);
}