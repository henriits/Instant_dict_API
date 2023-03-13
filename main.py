import api, dokumentation
import justpy as jp


jp.Route("/api", api.Api.serve)
jp.Route("/", dokumentation.Doc.serve)
jp.justpy()