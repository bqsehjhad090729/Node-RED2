[{"id":"edc5b90d.13f468","type":"tab","label":"Flow 5","disabled":false,"info":""},{"id":"b0a62fd1.5fa3a","type":"http in","z":"edc5b90d.13f468","name":"","url":"/pin4","method":"get","upload":false,"swaggerDoc":"","x":110,"y":180,"wires":[["7cdeeba.7f54614"]]},{"id":"94e4d3d4.70e4b","type":"rpi-gpio in","z":"edc5b90d.13f468","name":"GPIO4","pin":"7","intype":"up","debounce":"25","read":true,"x":110,"y":220,"wires":[["d6062271.a01e"]]},{"id":"d6062271.a01e","type":"function","z":"edc5b90d.13f468","name":"Set GPIO","func":"global.set(\"GPIO\", msg.payload)\nreturn msg;","outputs":1,"noerr":0,"x":330,"y":220,"wires":[["6a48737f.a3370c"]]},{"id":"7cdeeba.7f54614","type":"function","z":"edc5b90d.13f468","name":"Get GPIO","func":"msg.payload = global.get(\"GPIO\");\nreturn msg;","outputs":1,"noerr":0,"x":320,"y":180,"wires":[["e6b69a09.ac4158","6a48737f.a3370c"]]},{"id":"e6b69a09.ac4158","type":"http response","z":"edc5b90d.13f468","name":"","statusCode":"","headers":{},"x":490,"y":180,"wires":[]},{"id":"6a48737f.a3370c","type":"debug","z":"edc5b90d.13f468","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":540,"y":280,"wires":[]}]
