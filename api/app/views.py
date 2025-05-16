from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.deepseek import DeepSeekAnalyzer

analyzer = DeepSeekAnalyzer()

@api_view(['POST'])
def analyze_security(request):
    if not request.data.get('text'):
        return Response({"error": "Se requiere texto para analizar"}, status=400)
    
    result = analyzer.analyze_security_content(request.data['text'])
    
    if 'error' in result:
        return Response({"error": result['error']}, status=500)
    
    return Response({
        "result": result,
        "status": "success"
    })