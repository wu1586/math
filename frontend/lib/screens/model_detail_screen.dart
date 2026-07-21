import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../services/model_service.dart';
import '../models/model.dart';

class ModelDetailScreen extends StatelessWidget {
  final MathModel model;
  final ModelService modelService;

  const ModelDetailScreen({
    super.key,
    required this.model,
    required this.modelService,
  });

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        appBar: AppBar(
          title: Text(model.name),
          bottom: const TabBar(
            tabs: [
              Tab(icon: Icon(Icons.book), text: '理论'),
              Tab(icon: Icon(Icons.lightbulb), text: '案例'),
              Tab(icon: Icon(Icons.code), text: '代码'),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            // 理论标签页
            _buildContentTab(
              context,
              model.theoryContent ?? '暂无理论内容',
              Icons.book,
            ),
            // 案例标签页
            _buildContentTab(
              context,
              model.caseContent ?? '暂无案例内容',
              Icons.lightbulb,
            ),
            // 代码标签页
            _buildCodeTab(context),
          ],
        ),
      ),
    );
  }

  Widget _buildContentTab(BuildContext context, String content, IconData icon) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: SelectableText(
        content,
        style: const TextStyle(
          fontSize: 16,
          height: 1.6,
        ),
      ),
    );
  }

  Widget _buildCodeTab(BuildContext context) {
    final code = model.codeContent ?? '% 暂无代码示例';

    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(12),
          color: Colors.grey.shade200,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                'MATLAB代码',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                ),
              ),
              IconButton(
                icon: const Icon(Icons.copy),
                onPressed: () {
                  Clipboard.setData(ClipboardData(text: code));
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(
                      content: Text('代码已复制到剪贴板'),
                      duration: Duration(seconds: 2),
                    ),
                  );
                },
                tooltip: '复制代码',
              ),
            ],
          ),
        ),
        Expanded(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(16),
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.grey.shade50,
                borderRadius: BorderRadius.circular(8),
                border: Border.all(color: Colors.grey.shade300),
              ),
              child: SelectableText(
                code,
                style: const TextStyle(
                  fontFamily: 'monospace',
                  fontSize: 14,
                  height: 1.5,
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}
