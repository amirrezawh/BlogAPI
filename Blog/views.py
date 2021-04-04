from .models import Post,PostLike,Comments
from rest_framework import generics, status
from .serializer import PostSerializer, SaveLikeSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class ListPost(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class ShowPost(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UpdatePost(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def put(self, request, pk):
        post_id = Post.objects.get(id=pk)
        serializer = self.serializer_class(post_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response("Update failed.", status=status.HTTP_400_BAD_REQUEST)

class DeletePost(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def delete(self, request, pk):
        try:
            Post.objects.get(id=pk).delete()
            return Response("Post Deleted", status=status.HTTP_202_ACCEPTED)
        except Exception:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)



class SaveLike(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SaveLikeSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        if PostLike.objects.filter(like_user=data['like_user']).exists():
            return Response("You have already liked this post.", 
            status=status.HTTP_406_NOT_ACCEPTABLE)
        
        serializer.save()        
        return Response("Like saved successfully.", 
        status=status.HTTP_202_ACCEPTED)

class ShowLike(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        count_like = PostLike.objects.filter(like_post=pk).count()
        return Response(count_like, status=status.HTTP_200_OK)


class CreateComment(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

class ListComment(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

class ShowComment(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

class UpdateComment(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def put(self, request, pk):
        post_id = Comments.objects.get(id=pk)
        serializer = self.serializer_class(post_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response("Update failed.", status=status.HTTP_400_BAD_REQUEST)

class DeleteComment(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def delete(self, request, pk):
        try:
            Comments.objects.get(id=pk).delete()
            return Response("Comment Deleted", status=status.HTTP_202_ACCEPTED)
        except Exception:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
