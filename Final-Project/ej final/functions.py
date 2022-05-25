import http.client
import json
from pathlib import Path
import jinja2 as j
from Seq1 import Seq

SERVER = 'rest.ensembl.org'

genes_dict = {"SRCAP": "ENSG00000080603",
              "FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "RNU6_269P": "ENSG00000212379",
              "FXN": "ENSG00000165060",
              "MIR633": "ENSG00000207552",
              "TTTY4": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

def create_request(url, params):
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", url + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    # -- Print the received data
    #print(f"CONTENT: {data1}")
    return json.loads(data1)

def list_species(arguments):
    try:
        if int(arguments["number_species"][0]) > 310:
            contents = read_html_file("error.html") \
                .render(context={})
        else:
            if arguments == {}:
                n_species = "-1"
            elif arguments != {}:
                n_species = (arguments["number_species"][0])
            PARAMS = "/info/species?content-type=application/json"
            dict_answer = create_request(url="", params=PARAMS)
            list_species = dict_answer["species"]
            list_species = list_species[0:int(n_species)]
            list_species_2 = []
            for l in list_species:
                for k, v in l.items():
                    if k == "display_name":
                        list_species_2.append(v)
            contents = read_html_file("list_species.html") \
                .render(context={"species": list_species_2,
                        "n_species": len(list_species_2)})
    except ValueError:
        contents = read_html_file("error.html") \
            .render(context={})
    return contents

def karyotype(arguments):
    try:
        species = (arguments["species"][0])
        REQ = "/info/assembly/"
        PARAMS = "?content-type=application/json"
        dict_answer = create_request(url=REQ + species, params=PARAMS)
        karyotype = dict_answer["karyotype"]
        contents = read_html_file("karyotype.html") \
            .render(context={"species": species.upper(),
                             "karyotype": karyotype})
    except KeyError:
        contents = read_html_file("error.html") \
            .render(context={})
    return contents

def chromosome_length(arguments):
    try:
        species = (arguments["species"][0])
        chromo = (arguments["chromosome"][0])
        REQ = "/info/assembly/"
        PARAMS = "?content-type=application/json"
        dict_answer = create_request(url=REQ + species, params=PARAMS)
        try:
            for l in dict_answer["top_level_region"]:
                if l["name"] == chromo:
                    length = l["length"]
            contents = read_html_file("chromosome_length.html") \
                .render(context={"species": species,
                                 "chromosome": chromo,
                                 "length": length})
        except UnboundLocalError:
            contents = read_html_file("error.html") \
                .render(context={})
    except KeyError:
        contents = read_html_file("error.html") \
            .render(context={})
    return contents

def gene_seq(arguments):
    try:
        gene_name = (arguments["gene"][0])
        for gene, id in genes_dict.items():
            if gene == gene_name:
                REQ = "/sequence/id/"
                PARAMS = "?content-type=application/json"
                dict_answer = create_request(url=REQ + id, params=PARAMS)
                sequence = dict_answer["seq"]
                contents = read_html_file("gene_sequence.html") \
                    .render(context={"gene": gene_name,
                                     "sequence": sequence})

        return contents

    except UnboundLocalError:
        contents = read_html_file("error.html") \
                .render(context={})
        return contents
    except KeyError:
        contents = read_html_file("error.html") \
            .render(context={})
        return contents
def gene_info(arguments):
    try:
        gene_name = (arguments["gene"][0])
        for gene, id in genes_dict.items():
            if gene == gene_name:
                REQ = "/sequence/id/"
                PARAMS = "?content-type=application/json"
                dict_answer = create_request(url=REQ + id, params=PARAMS)
                sequence = dict_answer["seq"]
                id = dict_answer["id"]
                length = len(sequence)
                info = dict_answer["desc"]
                info = info.split(":")
                start = info[3]
                end = info[4]
                chromosome_name = info[1]
                contents = read_html_file("gene_info.html") \
                    .render(context={"gene": gene_name,
                                     "start": start,
                                     "end": end,
                                     "length": length,
                                     "id": id,
                                     "chromosome_name": chromosome_name})
        return contents
    except UnboundLocalError:
        contents = read_html_file("error.html") \
            .render(context={})
        return contents
    except KeyError:
        contents = read_html_file("error.html") \
            .render(context={})
        return contents

def gene_calc(arguments):
    try:
        gene_name = (arguments["gene"][0])
        for gene, id in genes_dict.items():
            if gene == gene_name:
                REQ = "/sequence/id/"
                PARAMS = "?content-type=application/json"
                dict_answer = create_request(url=REQ + id, params=PARAMS)
                sequence = dict_answer["seq"]
                s1 = Seq(sequence)
                calc = s1.info()
                calculations = calc.split("\n")
                length = calculations[0]
                base_a = calculations[1]
                base_c = calculations[2]
                base_g = calculations[3]
                base_t = calculations[4]
                contents = read_html_file("gene_calc.html") \
                    .render(context={"gene": gene_name,
                                     "length": length,
                                     "base_a": base_a,
                                     "base_c": base_c,
                                     "base_g": base_g,
                                     "base_t": base_t})
        return contents
    except UnboundLocalError:
        contents = read_html_file("error.html") \
            .render(context={})
        return contents
    except KeyError:
        contents = read_html_file("error.html") \
            .render(context={})
        return contents

def gene_list(arguments):
    try:
        chromo = (arguments["chromo"][0])
        start = (arguments["start"][0])
        end = (arguments["end"][0])
        REQ = "/phenotype/region/homo_sapiens/"
        PARAMS = "?content-type=application/json"
        list_answer = create_request(url=REQ + chromo + ":" + start + "-" + end, params=PARAMS)
        genes_list = []
        for l in list_answer:
            d = l["phenotype_associations"]
            try:
                for dict in d:
                    genes_list.append(dict["attributes"]["associated_gene"])
            except KeyError:
                pass
        contents = read_html_file("gene_list.html") \
            .render(context={"genes_list": genes_list,
                        "chromo": chromo,
                        "start": start,
                        "end": end})
        return contents
    except AttributeError:
        contents = read_html_file("error.html") \
            .render(context={})
        return contents
    except KeyError:
        contents = read_html_file("error.html") \
            .render(context={})
        return contents





