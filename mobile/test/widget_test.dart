import 'package:flutter_test/flutter_test.dart';
import 'package:mobile/main.dart';

void main() {
  testWidgets('App renders home screen test', (WidgetTester tester) async {
    await tester.pumpWidget(const DemansTakipApp());
    expect(find.byType(DemansTakipApp), findsOneWidget);
  });
}
