fetch = require("node-fetch");
fs = require('fs');

const convertPaths = (jsonSchema) => {
    Object.entries(jsonSchema.definitions).map(([key, definition], index) => {
      const newKey = definition["$id"].replace("#", "");
      const newRef = definition
      jsonSchema.definitions[newKey] = definition;
      delete jsonSchema.definitions[key];
    });
};

const loadJsonSchema = (jsonSchemaUrl, outputFile) => {
    console.log("Loading URL " + jsonSchemaUrl);
    fetch(jsonSchemaUrl)
      .then((res) => res.json())
      .then(
        (result) => {
          convertPaths(result);
          let output = JSON.stringify(result, null, 2);
          output = output.replace(/#assembly_/g, "#/definitions/assembly_");
          output = output.replace(/#field_/g, "#/definitions/field_");
          fs.writeFile(outputFile, output, function (err) {
            if (err) return console.log(err);
          });
          console.log("Converted output in " + outputFile);
        },
        (error) => {
          console.error(error);
        }
      );
};

const jsonSchemaUrl = process.argv[2];
const outputFile = process.argv[3];
const jsonSchema = loadJsonSchema(jsonSchemaUrl, outputFile);

