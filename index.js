const http = require('http');
const fs = require('fs');
const express = require('express');
const url = require('url');
const slugify = require('slugify');

const indexPage = fs.readFileSync(
    `${__dirname}/pages/index-page.html`,
    'utf-8'
);

const loginPage = fs.readFileSync(
    `${__dirname}/pages/login-page.html`,
    'utf-8'
);

const registerPage = fs.readFileSync(
    `${__dirname}/pages/register-page.html`,
    'utf-8'
);

//Server Starts Here:

const server = http.createServer((req,res)=>{
    const {query,pathname} = url.parse(req.url,true);
    console.log(`User asked for ${pathname}`)
    if(pathname === '/'){
        res.writeHead(200,{
            'Content-type': 'text/html'
        })
        const output = indexPage
                    .replace('{%DIR%}',__dirname)
                    .replace('{%TITLE%}','Home');
        res.end(output);
    }if(pathname === '/login'){
        res.writeHead(200,{
            'Content-type': 'text/html'
        })
        const output = loginPage
                    .replace('{%DIR%}',__dirname)
                    .replace('{%TITLE%}','Login');
        res.end(output);
    }if(pathname === '/register'){
        res.writeHead(200,{
            'Content-type': 'text/html'
        })
        const output = registerPage
                    .replace('{%DIR%}',__dirname)
                    .replace('{%TITLE%}','Register');
        res.end(output);
    }
})

server.listen(8199,'127.0.0.1',()=>{
    console.log('Listening...')
})