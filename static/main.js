function CopyToClipboard(){
    const e = document.getElementById("password-text")
    const copyText = e.innerHTML.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    navigator.clipboard.writeText(copyText);
}