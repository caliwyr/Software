// the endpoints: https://beamtic.com/user-agents/

let page = await fetch('https://beamtic.com/user-agents/')
let response = await page.text()

// parse all the user agents in div with class "dk_border dk_pad dk_mar"
let userAgents = response.match(/<div class="dk_border dk_pad dk_mar">(.+?)<\/div>/g)
let list = []
for(let i = 0; i < userAgents.length; i++) {
    let userAgent = {
        name: userAgents[i].match(/<b>(.+?)<\/b>/)[1],
        data: userAgents[i].split(':')[1]
    }

    // add the OS detection from data
    try {
        userAgent.os = userAgent.data.match(/\((.*?)\)/)[1]
    } catch (error) {
        userAgent.os = 'Unknown'
    }

    // Detect if the user agent is mobile or not
    if(userAgent.data.match(/(iPhone|iPod|iPad|Android|BlackBerry)/)) {
        userAgent.mobile = true
    } else {
        userAgent.mobile = false
    }

    list.push(userAgent)
}

console.log(list)

Deno.writeTextFileSync('./user-agents.json', JSON.stringify(list, null, 4))
